"""
ollama_client.py

This module provides a reusable function for interacting with local
LLM models through the Ollama API.

Purpose:
Avoid repeating the same Ollama request logic across multiple model files.
All models (Llama3, Mistral, Gemma) will call this shared function.
"""

import ollama


def run_model(model_name, prompt):
    """
    Sends a prompt to the specified LLM model via Ollama and returns the response.

    Parameters:
    model_name (str): Name of the model installed in Ollama (e.g., 'llama3', 'mistral', 'gemma:2b')
    prompt (str): The input prompt that will be sent to the model

    Returns:
    str: The generated response from the model
    """

    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]