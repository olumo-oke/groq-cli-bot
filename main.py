import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: GROQ_API_KEY not found in .env file.")
    exit()

client = Groq(api_key=api_key)

def run_chatbot():
    messages = [
        {"role": "system", "content": "You are a helpful assistant running in a CLI."}
    ]

    print("\n🚀 Groq CLI Chatbot Active! (Type 'exit' to stop)\n" + "-"*45)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                stream=True,
            )

            print("AI: ", end="", flush=True)
            full_response = ""

            for chunk in completion:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="", flush=True)
                    full_response += content
            
            print("\n" + "-"*45)

            messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    run_chatbot()