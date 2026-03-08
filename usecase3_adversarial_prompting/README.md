# GenAI Bootcamp – Use Case 3: Adversarial Prompting

This use case demonstrates how Large Language Models (LLMs) respond to adversarial prompts. The goal is to simulate common attack techniques used to manipulate or bypass model behavior and observe how the model reacts.

## Objective

To test the robustness and safety behavior of an LLM by executing different adversarial prompting techniques.

## Implemented Attacks

### 1. Prompt Injection
Attempts to override the original system instructions by inserting malicious instructions such as asking the model to ignore previous instructions.

### 2. Prompt Breaking
Attempts to force the model to deviate from the intended task by introducing conflicting instructions.

### 3. Jailbreaking
Attempts to bypass the model's safety restrictions by asking the model to act without limitations.

## Technologies Used

- Python
- Ollama
- Open-source LLM (e.g., Llama3)

## How to Run

1. Install and start **Ollama**

2. Pull the required model

```bash
ollama pull llama3
```
3. Run the Program
```bash
python main.py
```