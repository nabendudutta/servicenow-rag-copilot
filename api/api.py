from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

app = FastAPI()

db = FAISS.load_local("vectordb", OpenAIEmbeddings())
llm = ChatOpenAI(temperature=0)

class Q(BaseModel):
    question: str

@app.post("/chat")
def chat(q: Q):
    docs = db.similarity_search(q.question, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    answer = llm.predict(f"""
You are an IT incident assistant.

Context:
{context}

Question: {q.question}
Answer:
""")

    return {"answer": answer}