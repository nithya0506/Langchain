import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini model (use gemini-1.5-flash or gemini-pro)
chat = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-pro"
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

#  Ask a question
response = chat.invoke([
    HumanMessage(content="What is LangChain?")
])

#  Show the response
print(response.content)
