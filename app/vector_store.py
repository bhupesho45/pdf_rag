import faiss
import numpy as np

from load_pdf import load_pdf
from chunk import create_chunks
from embed import create_embeddings


def create_vector_store(embeddings):

    # Number of dimensions in each embedding
    dimension = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # FAISS expects float32
    embeddings = np.array(embeddings).astype("float32")

    # Add embeddings to FAISS
    index.add(embeddings)

    return index


if __name__ == "__main__":

    pdf_path = "data/document.pdf"

    # 1. Load PDF
    pages = load_pdf(pdf_path)

    # 2. Create chunks
    chunks = create_chunks(pages)

    # 3. Create embeddings
    embeddings = create_embeddings(chunks)

    # 4. Create FAISS index
    index = create_vector_store(embeddings)

    print("Number of vectors stored:", index.ntotal)
    print("Vector dimension:", index.d)