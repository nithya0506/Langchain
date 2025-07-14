from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:1b")  
result = llm.invoke("Give me a fact about Tamil:")
print(result)



# Generation method

# print("-------------------")
# print("LLM using Generate")
# print("-------------------")

# result = llm.generate(["Give me a fact about fullstack devops:,"
#                         "Give me a brief about llm"])
# # print(result.generations)
# print(result.generations[0][0].text)

