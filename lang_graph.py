import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

# Load Google API key from .env or set manually
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

# Create Gemini Chat model
chat = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY
)

# Define LangGraph state (input schema)
class InputState(BaseModel):
    input: str
    output: str = None 

# Node function must return a dict (not Pydantic object)
def ask_gemini(state: InputState) -> dict:
    print("Asking Gemini with:", state.input)
    response = chat.invoke([HumanMessage(content=state.input)])
    print("Raw Gemini Response Object:", response)
    return {"output": response.content}


# Build LangGraph
graph_builder = StateGraph(InputState)
graph_builder.add_node("ask_gemini", ask_gemini)
graph_builder.set_entry_point("ask_gemini")
graph_builder.add_edge("ask_gemini", END)
graph = graph_builder.compile()

# Run the graph
user_question = "What is LangGraph?"
final_state = graph.invoke({"input": user_question})

#  Access and print the result
print(" Gemini Response:", final_state.get("output", "No response returned."))


