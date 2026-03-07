import ollama
import numpy as np
import faiss
import os
from pdf_utils import extract_pdf_text

# --------------------------------------------------
# Step 1: Extract text from the PDF document
# --------------------------------------------------
# The PDF file is first loaded and converted into raw text.
#
# This step uses the helper function `extract_pdf_text`
# from pdf_utils.py, which utilizes the pdfplumber library
# to read each page of the document and extract its text.
#
# The extracted text will serve as the knowledge source
# for the Retrieval-Augmented Generation (RAG) pipeline.
#
# This step is separated into a utility module to keep
# the pipeline clean and modular.
# --------------------------------------------------

# --------------------------------------------------
# Step 2: Split the extracted document text into chunks
# --------------------------------------------------
# Large documents cannot be processed effectively in one
# prompt due to token limits of LLMs. Therefore, the text
# is divided into smaller segments (chunks).
#
# Each chunk represents a portion of the document that
# can later be embedded and stored in the vector database.
#
# chunk_size controls the number of characters per chunk.
# This simple implementation uses character-based splitting,
# which is sufficient for demonstration purposes.
# --------------------------------------------------
def chunk_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])

    return chunks


# --------------------------------------------------
# Step 3: Generate vector embeddings for each chunk
# --------------------------------------------------
# Embeddings convert text into numerical vectors that
# represent semantic meaning.
#
# Similar texts produce similar vector representations.
#
# These embeddings allow us to perform similarity search
# later when retrieving relevant information from the
# document.
#
# This implementation uses the Ollama embedding model:
# "nomic-embed-text"
# --------------------------------------------------
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]


# --------------------------------------------------
# Step 4: Build the vector database (FAISS index)
# --------------------------------------------------
# After generating embeddings for all text chunks,
# they are stored in a vector database.
#
# FAISS (Facebook AI Similarity Search) is used here
# to efficiently perform similarity search between
# vectors.
#
# IndexFlatL2 calculates Euclidean distance between
# embeddings to determine similarity.
#
# The vector database will later allow us to retrieve
# the most relevant chunks when a question is asked.
# --------------------------------------------------
def build_vector_db(chunks):

    # Generate embeddings for all chunks
    embeddings = [get_embedding(chunk) for chunk in chunks]

    # Determine vector dimensionality
    dimension = len(embeddings[0])

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Convert embeddings into numpy array and store in index
    index.add(np.array(embeddings).astype("float32"))

    return index, embeddings


# --------------------------------------------------
# Step 5: Retrieve the most relevant chunks
# --------------------------------------------------
# When a user asks a question, the question is also
# converted into an embedding.
#
# The embedding is compared with all stored chunk
# embeddings using the FAISS index.
#
# The top_k most similar chunks are retrieved and
# used as context for the LLM.
#
# This is the core retrieval step of the RAG pipeline.
# --------------------------------------------------
def retrieve_chunks(question, chunks, index, top_k=3):

    # Convert the question into an embedding
    question_embedding = np.array([get_embedding(question)]).astype("float32")

    # Search FAISS index for the closest vectors
    distances, indices = index.search(question_embedding, top_k)

    # Retrieve the corresponding chunks
    retrieved_chunks = [chunks[i] for i in indices[0]]

    return retrieved_chunks


# --------------------------------------------------
# Step 6: Generate the final answer using the LLM
# --------------------------------------------------
# The retrieved chunks are combined and used as context
# for the LLM.
#
# The LLM uses this contextual information to generate
# a more accurate answer grounded in the document.
#
# This step is known as "Generation" in Retrieval
# Augmented Generation (RAG).
#
# The prompt instructs the LLM to return the answer
# in JSON format for structured output.
# --------------------------------------------------
def ask_llm(question, context):

    prompt = f"""
You are an AI assistant.

Use the context below to answer the question.

Return the answer in JSON format.

Example:
{{
 "answer": ""
}}

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# --------------------------------------------------
# MAIN RAG PIPELINE
# --------------------------------------------------
# This section orchestrates the entire RAG workflow:
#
# 1. Load and extract text from the PDF document
# 2. Split the document into smaller chunks
# 3. Generate embeddings for each chunk
# 4. Store embeddings in a FAISS vector database
# 5. Convert the user question into an embedding
# 6. Retrieve the most relevant chunks
# 7. Send retrieved context to the LLM
# 8. Generate the final answer
# --------------------------------------------------

# Get the current script directory
BASE_DIR = os.path.dirname(__file__)

# Construct the absolute path to the PDF file
pdf_path = os.path.join(BASE_DIR, "sample.pdf")

# Step 1: Extract text from the PDF document
document_text = extract_pdf_text(pdf_path)

# Step 2: Split the document into chunks
# Only the first 10 chunks are used to limit processing
chunks = chunk_text(document_text)[:10]

# Step 3–4: Build the vector database
index, embeddings = build_vector_db(chunks)

# Define the user question
question = "What is Accenture's purpose?"

# Step 5: Retrieve relevant chunks based on the question
retrieved_chunks = retrieve_chunks(question, chunks, index)

# Combine retrieved chunks into a single context string
context = "\n".join(retrieved_chunks)

# Step 6: Generate the final answer using the LLM
answer = ask_llm(question, context)

# Display the result
print("\n=== RAG Answer ===\n")
print(answer)