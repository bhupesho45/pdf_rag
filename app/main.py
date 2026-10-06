from load_pdf import load_pdf
from chunk import create_chunks
from embed import create_embeddings, model
from vector_store import create_vector_store
from retrieve import retrieve
from context import build_context
from generate import generate_answer


def main():

    pdf_path = "data/document.pdf"

    # 1. Load PDF
    pages = load_pdf(pdf_path)

    # 2. Create chunks
    chunks = create_chunks(pages)

    # 3. Create embeddings
    embeddings = create_embeddings(chunks)

    # 4. Create FAISS index
    index = create_vector_store(embeddings)

    # 5. Ask question
    question = input("\nAsk a question: ")

    # 6. Retrieve relevant chunks
    results = retrieve(
        question,
        chunks,
        index,
        model,
        top_k=3
    )

    # 7. Build context
    context = build_context(results)

    # 8. Generate answer
    answer = generate_answer(
        question,
        context
    )

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)

    print("\n" + "=" * 60)
    print("CONTEXT USED")
    print("=" * 60)

    print(context)


if __name__ == "__main__":
    main()

