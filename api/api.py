from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

app = FastAPI()

db = FAISS.load_local("vectordb", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
llm = ChatOpenAI(temperature=0)

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(q: Query):
    docs = db.similarity_search(q.question, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    response = llm.invoke(
        f"""
You are a ServiceNow incident assistant.

Context:
{context}

Question:
{q.question}

Answer clearly:
"""
    )

    return {
        "answer": response.content
    }