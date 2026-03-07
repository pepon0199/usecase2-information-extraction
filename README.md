# GenAI PDF Information Extraction (CAG vs RAG)

This project demonstrates how to extract structured insights from a PDF
document using **Large Language Models (LLMs)**.

Two GenAI architectures are implemented and compared:

-   **Context-Augmented Generation (CAG)**
-   **Retrieval-Augmented Generation (RAG)**

The system runs locally using **Ollama** with the **Llama3** model.

------------------------------------------------------------------------

# Project Goal

Perform **Information Extraction (IE)** from a PDF document and generate
structured insights such as:

-   Company name
-   Purpose
-   Industry
-   Mission
-   Key services
-   Technologies used

------------------------------------------------------------------------

# Architecture Overview

## CAG (Context-Augmented Generation)

Entire document text is sent directly to the LLM.

Workflow:

PDF → Text Extraction → Prompt → LLM → JSON Output

## RAG (Retrieval-Augmented Generation)

Only relevant parts of the document are retrieved before sending to the
LLM.

Workflow:

PDF → Text Extraction → Chunking → Embeddings → Vector DB → Retrieval →
LLM → Answer

------------------------------------------------------------------------

# Technologies Used

-   Python
-   Ollama
-   Llama3
-   pdfplumber
-   FAISS
-   NumPy

------------------------------------------------------------------------

# Setup

Install dependencies:

pip install -r requirements.txt

Install Ollama:

https://ollama.com

Pull required models:

ollama pull llama3 ollama pull nomic-embed-text

------------------------------------------------------------------------

# Run the Pipelines

Run CAG:

python cag_pipeline.py

Run RAG:

python rag_pipeline.py

------------------------------------------------------------------------

# GPU Issue (Optional Fix)

If you encounter:

llama runner process has terminated: CUDA error

Disable GPU temporarily:

Windows: set OLLAMA_NO_GPU=1

Mac/Linux: export OLLAMA_NO_GPU=1

------------------------------------------------------------------------

# Author

Karl Pepon Ayala\
GenAI Bootcamp Assignment
