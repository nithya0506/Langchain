from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Simple string-based prompt
pt = PromptTemplate.from_template("Tell me a {adjective} joke about {content}")
print(pt.format(adjective="funny", content="penguins"))

# Chat prompt with system and dynamic user messages
chat_pt = ChatPromptTemplate.from_messages([
  ("system", "You are a translator."),
  ("user", "{text}")
])
print(chat_pt.format(text="Hello, world!"))

# Prompt with conversation history placeholder
chat_pt2 = ChatPromptTemplate.from_messages([
  ("system", "You are helpful."),
  MessagesPlaceholder("history"),
  ("user", "{query}")
])

#  Valid message history
history = [
    HumanMessage(content="What is the speed of light?"),
    AIMessage(content="Approximately 299,792,458 meters per second.")
]

#  Pass formatted history
print(chat_pt2.format(history=history, query="Explain relativity"))
