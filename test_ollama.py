import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {"role": "user", "content": "What is the purpose of Accenture?"}
    ]
)

print(response['message']['content'])