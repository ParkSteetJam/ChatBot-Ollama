import ollama

client = ollama.Client()
MODEL = "gemma4:e4b"


while True:
    prompt = input("Enter your prompt: ")

    def chatAI(prompt):
        response = client.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response

    print(chatAI(prompt).message.content)

    if prompt.lower() == "quit":
        print("Bot: Goodbye!")
        break

