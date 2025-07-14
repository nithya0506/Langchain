from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("assets/Grammar.pdf")
pages = loader.load_and_split() # Divides the data into chunks

# print(pages)
print(pages[0].page_content) 
#single chunk