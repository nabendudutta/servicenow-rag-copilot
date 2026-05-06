import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# ensure API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

loader = DirectoryLoader("data/markdown")
docs = loader.load()

chunks = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
).split_documents(docs)

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(chunks, embeddings)
db.save_local("vectordb")

print("Vector DB built successfully")