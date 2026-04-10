from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import  HumanMessage
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support assistant."),
    MessagesPlaceholder(variable_name='chat_history'), 
    ('human', '{customer_query}')
])


#load chat History
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#Create Prompt 

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'customer_query': "Where is my refund ?"
})

print(prompt.messages)