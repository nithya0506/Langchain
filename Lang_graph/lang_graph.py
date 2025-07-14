from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

# Create LLaMA 3.2 (1B) Chat model from Ollama
chat = ChatOllama(model="llama3.2:1b")  

# Define LangGraph state (input schema)
class InputState(BaseModel):
    input: str
    output: str = None 

# Node function must return a dict (not Pydantic object)
def ask_llama(state: InputState) -> dict:
    print("Asking LLaMA 3.2:", state.input)
    response = chat.invoke([HumanMessage(content=state.input)])
    print("Raw LLaMA Response Object:", response)
    return {"output": response.content}

# Build LangGraph
graph_builder = StateGraph(InputState)
graph_builder.add_node("ask_llama", ask_llama)
graph_builder.set_entry_point("ask_llama")
graph_builder.add_edge("ask_llama", END)
graph = graph_builder.compile()

# Run the graph
user_question = "What is LangGraph?"
final_state = graph.invoke({"input": user_question})

# Print the result
print("LLaMA Response:", final_state.get("output", "No response returned."))
