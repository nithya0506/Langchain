import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load the .env file
load_dotenv()

# Get the API key safely
google_api_key = os.environ["GOOGLE_API_KEY"]

# Initialize Gemini model
chat = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key
)

# Run a test
response = chat.invoke([HumanMessage(content="Hello Gemini!")])
print(response.content)
