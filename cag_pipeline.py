import ollama
import os
from pdf_utils import extract_pdf_text


# --------------------------------------------------
# Step 1: Extract text from the PDF document
# --------------------------------------------------
# The first step in the pipeline is to load the PDF file
# and convert its contents into plain text.
#
# This is done using the helper function `extract_pdf_text`
# from the `pdf_utils.py` module. That function utilizes
# the pdfplumber library to iterate through each page
# of the PDF and extract readable text.
#
# The extracted text will serve as the primary input
# to the Large Language Model (LLM) for analysis.
#
# Unlike RAG, CAG sends the entire document directly
# to the LLM without performing chunking, embeddings,
# or vector retrieval.
# --------------------------------------------------

# Determine the directory of the current script
BASE_DIR = os.path.dirname(__file__)

# Build the full path to the sample PDF document
pdf_path = os.path.join(BASE_DIR, "sample.pdf")

# Extract the full document text
document_text = extract_pdf_text(pdf_path)


# --------------------------------------------------
# Step 2: Create the prompt for the LLM
# --------------------------------------------------
# In the Context-Augmented Generation (CAG) approach,
# the entire document text is directly included in
# the prompt and sent to the LLM.
#
# The prompt instructs the model to analyze the
# document and extract key structured information.
#
# The response format is constrained to JSON to make
# the output structured and easier to process or
# store in downstream applications.
#
# The expected JSON structure includes:
#   - company_name
#   - purpose
#   - industry
#   - mission
#   - key_services
#   - technologies
#
# The extracted document text is embedded into the
# prompt using Python's f-string formatting.
# --------------------------------------------------
prompt = f"""
You are an expert document analyst.

Analyze the document and extract the key information.

Return the result ONLY in JSON format.

Example format:

{{
  "company_name": "",
  "purpose": "",
  "industry": "",
  "mission": "",
  "key_services": [],
  "technologies": []
}}

Document:
{document_text}
"""


# --------------------------------------------------
# Step 3: Send the prompt to the LLM
# --------------------------------------------------
# The prepared prompt is sent to the LLM using the
# Ollama chat API.
#
# The model used in this implementation is "llama3",
# which runs locally through Ollama.
#
# The LLM processes the prompt and generates a
# structured JSON response containing the extracted
# insights from the document.
# --------------------------------------------------
response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": prompt}
    ]
)


# --------------------------------------------------
# Step 4: Display the extracted insights
# --------------------------------------------------
# The response returned by the Ollama API contains
# the generated message from the model.
#
# The JSON result produced by the LLM is printed
# to the console for inspection.
# --------------------------------------------------
print("\n=== Extracted Insights ===\n")
print(response["message"]["content"])