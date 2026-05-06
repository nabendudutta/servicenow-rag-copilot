from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

loader = DirectoryLoader("data/markdown")
docs = loader.load()

chunks = CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

db = FAISS.from_documents(chunks, OpenAIEmbeddings())
db.save_local("vectordb")

print("Vector DB built")