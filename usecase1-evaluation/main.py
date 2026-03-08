"""
main.py

This is the main orchestration script of the LLM evaluation system.

Workflow:
1. Send the same prompt to two different models (Llama3 and Mistral).
2. Collect their responses.
3. Send both responses to a third model (Gemma) for evaluation.
4. Display the results to the user.

This demonstrates a simple LLM evaluation pipeline using the
"LLM-as-a-Judge" approach.
"""

from prompts import medical_prompt
from models.llama_model import get_llama_response
from models.mistral_model import get_mistral_response
from evaluator.gemma_evaluator import evaluate_responses


# Step 1: Generate response from Llama3
print("Running Llama3...")
llama_output = get_llama_response(medical_prompt)


# Step 2: Generate response from Mistral
print("Running Mistral...")
mistral_output = get_mistral_response(medical_prompt)


# Step 3: Display both model responses
print("\n==============================")
print("LLAMA3 RESPONSE")
print("==============================\n")
print(llama_output)

print("\n==============================")
print("MISTRAL RESPONSE")
print("==============================\n")
print(mistral_output)


# Step 4: Evaluate responses using Gemma
print("\nRunning evaluation using Gemma...\n")
evaluation_result = evaluate_responses(llama_output, mistral_output)


# Step 5: Display evaluation result
print("\n==============================")
print("EVALUATION RESULT (GEMMA)")
print("==============================\n")
print(evaluation_result)