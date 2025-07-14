
import os

from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WikipediaLoader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

current_dir = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(current_dir, "db")


output_parser = StrOutputParser()
model = ChatOllama(model="llama3.2:1b")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

print("------------------------------------")
print("Fetching data from WikipediaLoader:-")
print("------------------------------------")
documents = WikipediaLoader(query="Ratan Tata", load_max_docs=2).load()
print(documents)


print("--------------------------------------------")
print("Splitting data using CharacterTextSplitter:-")
print("--------------------------------------------")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200)  # 1st chunk = 800 2nd chunk = 801 to 1800 because of overlap
docs = text_splitter.split_documents(documents=documents)
print(docs)


print("-----------------------------------------")
print("Embedding docs and storing in Chroma db:-")
print("-----------------------------------------")
db_connection = Chroma.from_documents(documents=docs,
                                      embedding=embeddings,
                                      persist_directory=persist_directory)
print("Embedding Successfull!!!")


print("--------------------------------")
print("Retrieving docs from Chroma db:-")
print("--------------------------------")
retriever = db_connection.as_retriever()
response = retriever.invoke("When was Ratan Tata born?")
print(response)


print("-------------------------------------")
print("Getting answer from db using Model :-")
print("-------------------------------------")
prompt_template = PromptTemplate(
    input_variables=["document"],
    template="Answer any question from this document: {document}. When was Ratan Tata born?")
chain = prompt_template | model | output_parser
result = chain.invoke({"document": response[0].page_content})
print(result)