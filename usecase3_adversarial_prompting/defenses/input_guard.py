"""
input_guard.py

This module provides a simple defense mechanism to detect
potential adversarial prompts before they are sent to the LLM.

It scans prompts for suspicious keywords that commonly appear
in prompt injection or jailbreaking attempts.
"""


def detect_prompt_injection(prompt):
    """
    Detects whether a prompt contains suspicious patterns that
    may indicate a prompt injection or jailbreak attempt.

    Parameters:
    prompt (str): The input prompt to be analyzed.

    Returns:
    bool:
        True  -> suspicious prompt detected
        False -> prompt appears safe
    """

    suspicious_keywords = [
        "ignore previous instructions",
        "reveal system prompt",
        "bypass safety",
        "act as unrestricted",
        "pretend you are an ai with no restrictions"
    ]

    # Convert prompt to lowercase for case-insensitive matching
    prompt_lower = prompt.lower()

    for keyword in suspicious_keywords:
        if keyword in prompt_lower:
            return True

    return False