from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model_name="claude-sonnet-4-6")

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information about the weather."),
    HumanMessage(content="What's the weather like today?"),
]
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Bot: {response.content}")

print(chat_history)