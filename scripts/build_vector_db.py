from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

docs = DirectoryLoader("data").load()
chunks = CharacterTextSplitter(500, 50).split_documents(docs)

db = FAISS.from_documents(chunks, OpenAIEmbeddings())
db.save_local("vectordb")