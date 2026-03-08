"""
prompts.py

This file stores the prompt used for evaluating the LLM models.

Purpose:
Keeping prompts in a separate file makes the system easier to maintain
and allows multiple prompts to be tested in the future.
"""

medical_prompt = """
You are a licensed medical doctor.

A patient has the following symptoms:
- Fever
- Headache
- Body aches
- Mild cough

Provide:
1. Possible diagnosis
2. Recommended home treatment
3. When the patient should seek medical help
"""