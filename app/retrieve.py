import numpy as np

from load_pdf import load_pdf
from chunk import create_chunks
from embed import create_embeddings
from vector_store import create_vector_store


def retrieve(question, chunks, index, embedding_model, top_k=3):

    # Convert question into an embedding
    question_embedding = embedding_model.encode([question])

    # FAISS expects float32
    question_embedding = np.array(
        question_embedding
    ).astype("float32")

    # Search FAISS
    distances, indices = index.search(
        question_embedding,
        top_k
    )

    results = []

    for distance, index_position in zip(
        distances[0],
        indices[0]
    ):

        results.append({
            "chunk": chunks[index_position],
            "distance": float(distance)
        })

    return results


if __name__ == "__main__":

    pdf_path = "data/document.pdf"

    # Load PDF
    pages = load_pdf(pdf_path)

    # Create chunks
    chunks = create_chunks(pages)

    # Create embeddings
    embeddings = create_embeddings(chunks)

    # Create FAISS index
    index = create_vector_store(embeddings)

    # Import embedding model from embed.py
    from embed import model

    # Ask a question
    question = input("\nAsk a question: ")

    results = retrieve(
        question,
        chunks,
        index,
        model,
        top_k=3
    )

    print("\n\nRETRIEVED RESULTS")
    print("=" * 60)

    for i, result in enumerate(results):

        print("\nRESULT:", i + 1)
        print("Distance:", result["distance"])
        print("Page:", result["chunk"]["page"])
        print("Text:")
        print(result["chunk"]["text"])