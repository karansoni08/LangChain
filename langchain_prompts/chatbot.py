from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model_name="claude-sonnet-4-6")
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": response.content})
    print(f"Bot: {response.content}")

print(chat_history)