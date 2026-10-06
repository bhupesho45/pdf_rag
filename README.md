# PDF RAG

A simple Retrieval-Augmented Generation (RAG) project for asking questions about the content of a PDF document. The app reads a PDF, splits the text into chunks, creates embeddings, stores them in a FAISS vector index, retrieves the most relevant chunks, and then sends the retrieved context to a Groq-backed language model for answer generation.

## Overview

This project demonstrates a lightweight end-to-end RAG workflow using:

- PyMuPDF (`fitz`) for PDF extraction
- Sentence Transformers for embeddings
- FAISS for vector similarity search
- Groq-hosted OpenAI-compatible API for answer generation
- Python for the orchestration pipeline

## Project structure

```text
pdf_rag/
├── app/
│   ├── .env
│   ├── chunk.py
│   ├── context.py
│   ├── embed.py
│   ├── generate.py
│   ├── load_pdf.py
│   ├── main.py
│   ├── retrieve.py
│   └── vector_store.py
├── data/
│   └── document.pdf
├── venv/
├── .gitignore
└── README.md
```

## How it works

The pipeline in `app/main.py` follows this sequence:

1. Load the PDF file from `data/document.pdf`
2. Extract text from each page
3. Split pages into text chunks
4. Generate embeddings for each chunk
5. Build a FAISS vector index
6. Accept a user question
7. Retrieve the most relevant chunks
8. Build context from the retrieved chunks
9. Ask the LLM to answer using only that context

## Prerequisites

- Python 3.10+
- A Groq API key
- Internet access to call the Groq API

## Setup

1. Open a terminal in the project root.
2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

3. Install the required packages:

```bash
pip install pymupdf python-dotenv openai sentence-transformers faiss-cpu numpy
```

4. Add your Groq API key in the app environment file:

Create or update `app/.env` with:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the app

From the project root:

```bash
cd app
python main.py
```

When prompted, enter a question about the PDF content.

The app reads the PDF from:

```text
data/document.pdf
```

So make sure that file is present before running the app.

## Example

```text
Ask a question: What is the main topic of this document?
```

The app will output:

- The answer generated from the retrieved document context
- The context chunks used to generate the answer

## Notes

- This project rebuilds the vector store every time it runs.
- It does not persist the index to disk for later reuse.
- The LLM answer is grounded only in the retrieved document chunks, not in the full PDF.
- The current implementation uses `openai/gpt-oss-20b` through Groq's OpenAI-compatible endpoint.

## File responsibilities

- `app/load_pdf.py` — extracts text from PDF pages
- `app/chunk.py` — splits text into chunks with overlap
- `app/embed.py` — creates embeddings using Sentence Transformers
- `app/vector_store.py` — builds the FAISS index
- `app/retrieve.py` — retrieves top matching chunks
- `app/context.py` — formats the retrieved chunks as context
- `app/generate.py` — calls the Groq model to generate an answer
- `app/main.py` — orchestrates the full workflow

## License

This project does not currently include a license file. If you plan to share or publish it, add an appropriate license before distribution.
