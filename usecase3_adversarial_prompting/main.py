"""
main.py

Entry point of the Adversarial Prompting Use Case.

This script runs three different adversarial attack simulations:
1. Prompt Injection
2. Prompt Breaking
3. Jailbreaking

The results from the LLM are printed to the console so the user
can observe how the model reacts to adversarial prompts.
"""

from attacks.prompt_injection import run_prompt_injection
from attacks.prompt_breaking import run_prompt_breaking
from attacks.jailbreaking import run_jailbreak


def main():
    """
    Executes all adversarial prompting tests and prints the results.
    """

    print("\n==============================")
    print("Prompt Injection Test")
    print("==============================")

    injection_result = run_prompt_injection()
    print(injection_result)

    print("\n==============================")
    print("Prompt Breaking Test")
    print("==============================")

    breaking_result = run_prompt_breaking()
    print(breaking_result)

    print("\n==============================")
    print("Jailbreaking Test")
    print("==============================")

    jailbreak_result = run_jailbreak()
    print(jailbreak_result)


if __name__ == "__main__":
    main()