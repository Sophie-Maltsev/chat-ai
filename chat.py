from openai import OpenAI
import os

client = OpenAI(
    base_url=os.getenv("BASE_URL", "http://localhost:11434/v1"),
    api_key="ollama"
)

MODEL_NAME = "qwen2.5:3b"

messages = [
    {"role": "system", "content": "Ты дружелюбный помощник. Отвечай только на русском языке."}
]

print(f"Чат запущен.\n Модель: {MODEL_NAME}.\n Напишите 'выход' для завершения \n")

while True:
    user_input = input("Вы: ")
    user_input = user_input.encode("utf-8", errors="ignore").decode("utf-8")
    if user_input.strip().lower() in ['выход', 'exit']:
        print("До свидания!")
        break
    if not user_input.strip():
        continue

    messages.append({"role": "user", "content": user_input})

    print("ИИ: ", end="", flush=True)

    try:
        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )

        full_reply = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_reply += content

        print("\n")

        messages.append({"role":"assistant", "content": full_reply})

    except Exception as e:
        print(f"\nОшибка подключения к Ollama: {e}")
    