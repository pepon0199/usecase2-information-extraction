"""
llama_model.py

This module handles interactions with the Llama3 model.

Purpose:
Encapsulate the logic for generating responses from Llama3 so that
the main program can call it easily without worrying about model details.
"""

from utils.ollama_client import run_model


def get_llama_response(prompt):
    """
    Sends the prompt to the Llama3 model and returns its response.

    Parameters:
    prompt (str): The input prompt describing the medical scenario.

    Returns:
    str: Llama3's generated response.
    """

    return run_model("llama3", prompt)