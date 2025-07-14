# Import the prompt templates
from langchain_core.prompts import (PromptTemplate,
                                    ChatPromptTemplate,
                                    SystemMessagePromptTemplate,
                                    HumanMessagePromptTemplate)

# Import the parser, llm and chat ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_ollama.llms import OllamaLLM

#Initialise the model & templates
model = OllamaLLM(model="llama3.2:1b")
template = PromptTemplate(
    input_variables = ["topic"],
    template="Tell the fact about {topic}"
)

# print("-----------------------------------")
# print("Prompt template without using chain")
# print("-----------------------------------")

# prompt = template.format(topic = "Science")
# result = model.invoke(prompt)
# print(result)


# print("--------------------------------")
# print("Prompt template with using chain")
# print("--------------------------------")
# # Chaing 
# chain = template | model
# result= chain.invoke({"topic= histroy"}) # passing dynamic input
# print(result)

system_template = "You are an AI recipe assistant that specializes in {dietary_preference} dishes that can be prepared in {cooking_time}."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{recipe_request}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

# print("-----------------------------------------------")
# print(" chat model Prompt template without using chain")
# print("-----------------------------------------------")

# prompt = chat_prompt.format_prompt(cooking_time="15 min",
#                                    dietary_preference="Vegan", recipe_request="Quick Snack").to_messages()

# result = model.invoke(prompt)
# print(result)

print("-----------------------------------------------")
print(" chat model Prompt template using chain & output parser")
print("-----------------------------------------------")

chain = chat_prompt | model | StrOutputParser()

result = chain.invoke({"cooking_time":"15 min",
                                  "dietary_preference" : "Vegan", "recipe_request":"Quick Snack"})
print(result)