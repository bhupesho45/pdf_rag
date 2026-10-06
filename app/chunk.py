from load_pdf import load_pdf


def create_chunks(pages, chunk_size=50, chunk_overlap=5):

    chunks = []

    for page in pages:

        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "page": page_number
            })

            start += chunk_size - chunk_overlap

    return chunks


if __name__ == "__main__":

    pdf_path = "data/document.pdf"

    pages = load_pdf(pdf_path)

    chunks = create_chunks(pages)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:5]):

        print("\n" + "=" * 60)
        print("CHUNK:", i)
        print("PAGE:", chunk["page"])
        print("=" * 60)

        print(chunk["text"])