# LLM Evaluation Pipeline (GenAI Use Case)

This project demonstrates an evaluation workflow for Large Language Models (LLMs) using a multi-model comparison approach.

The system compares responses from two open-source LLM models and evaluates them using a third model acting as an unbiased evaluator.

## Models Used

- **Llama3** – Model A
- **Mistral** – Model B
- **Gemma (2B)** – Evaluator Model

All models are executed locally using **Ollama**.

---

## Objective

The goal of this use case is to demonstrate how LLM outputs can be evaluated by another LLM using predefined evaluation criteria.

This approach follows the **LLM-as-a-Judge evaluation method**, which is commonly used in modern AI benchmarking.

---

## Evaluation Criteria

The evaluator analyzes both model responses based on the following criteria:

- Accuracy
- Completeness
- Clarity
- Safety

The evaluator then determines which model produced the better response.

---
## Workflow

User Prompt  
↓  
Python Script  
↓  
Llama3 → Response A  
Mistral → Response B  
↓  
Gemma (Evaluator)  
↓  
Final Evaluation Result

## Installation

### 1 Install Ollama

Download and install Ollama:

https://ollama.com

Verify installation:

```bash
ollama --version
```
### 2 Pull Required Models
```bash
ollama pull llama3
ollama pull mistral
ollama pull gemma:2b
```

### 3 Install Python Dependencies
pip install -r requirements.txt

## Running the Project
python main.py

## Example Output
```bash
LLAMA3 RESPONSE
...

MISTRAL RESPONSE
...

EVALUATION RESULT (GEMMA)
Accuracy:
Response A: 8
Response B: 7

Final Winner:
Response A
```
## Author
Karl Pepon Ayala\
GenAI Bootcamp Assignment