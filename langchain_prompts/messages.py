from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model_name="claude-sonnet-4-6")

messages = [
    SystemMessage(content="You are a helpful assistant that provides information about the weather."),
    HumanMessage(content="What's the weather like today?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)