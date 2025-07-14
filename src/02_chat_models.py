from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, SystemMessage


# Chat object
chat = ChatOllama(model="llama3.2:1b")  

# print("-------------------")
# print("Chat Model with human message")
# print("-------------------")

# result = chat.invoke([HumanMessage(content="what is your name?")])

# print(result.content)

# Chat with Human & system message

# print("-------------------")
# print("Chat Model with human & system message")
# print("-------------------")

# result = chat.invoke([SystemMessage (content ="Imagine you are a Doctor"),
#                       HumanMessage (content ="Can you give me the health food tips?" )
#                       ])
# print(result.content)

print("--------------------------------------------------------------")
print("Chat Model with human & system message using generate function")
print("--------------------------------------------------------------")

result = chat.generate([[SystemMessage (content ="Imagine you are a Doctor"),
                      HumanMessage (content ="Can you give me the health food tips?" )]
                      ])
print(result.generations[0][0].text)