import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = OpenAI("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")
def main():
    system_prompt = "You are a helpful assistant."
    user_input = input("Enter your prompt: ")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    assistant_reply = response.choices[0].message.content
    total_tokens = response.usage.total_tokens

    print("\nAssistant's Reply:")
    print(assistant_reply)
    print(f"\nTotal Tokens Used: {total_tokens}")

if __name__ == "__main__":
    main()
