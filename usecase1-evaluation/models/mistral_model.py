"""
mistral_model.py

This module manages interaction with the Mistral model.

Purpose:
Allow the evaluation system to generate a response from the Mistral model
using the same prompt provided to Llama3.
"""

from utils.ollama_client import run_model


def get_mistral_response(prompt):
    """
    Sends the prompt to the Mistral model and returns its response.

    Parameters:
    prompt (str): The same evaluation prompt used for other models.

    Returns:
    str: Mistral's generated response.
    """

    return run_model("mistral", prompt)