from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2:1b") 

# print("-------------------")
# print("Prompt template using No input:")
# print("-------------------")

# no_input_prompt = PromptTemplate(input_variables = [], template=("Tell me a fact"))
# prompt = no_input_prompt.format()
# result = llm.invoke(prompt)
# print(result)

# print("-------------------")
# print("Prompt template using with input:")
# print("-------------------")

# no_input_prompt = PromptTemplate(input_variables = ["topic"], template=("Tell me a fact {topic}"))
# prompt = no_input_prompt.format(topic = "Agriculture")
# result = llm.invoke(prompt)
# print(result)

print("-------------------")
print("Prompt template using with multiple input:")
print("-------------------")

input_prompt = PromptTemplate(input_variables = ["topic", "level"], template=("Tell me a fact {topic} for a student {level} level"))
prompt = input_prompt.format(topic = "English", level = "teacher")
result = llm.invoke(prompt)
print(result)