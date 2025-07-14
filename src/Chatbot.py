from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template
template = """Here is the conversation history: {context}
Question = {question}
Answer:"""

# Initialize the model
model = OllamaLLM(model="llama3.2:1b")

prompt = ChatPromptTemplate.from_template(template)

# Function for handling conversation
def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break    

        # Step 1: Format the prompt
        formatted_prompt = prompt.format(context=context, question=user_input)

        # Step 2: Pass the string to the model
        result = model.invoke(formatted_prompt)

        print("Bot:", result)

        # Update context
        context += f"\nUser: {user_input}\nAI: {result}"

# Main block
if __name__ == "__main__":
    handle_conversation()
