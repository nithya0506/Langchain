from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader("assets/Daily_tracker.csv", encoding="UTF-8")
data = loader.load()

# print(data) print all data
print(data[5].page_content)
