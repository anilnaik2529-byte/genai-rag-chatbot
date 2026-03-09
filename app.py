from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from vector_store import search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    sessionId: str
    message: str


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/api/chat")
def chat(req: ChatRequest):

    results = search(req.message)

    if len(results) == 0:
        reply = "Sorry, I couldn't find relevant information."
    else:
        reply = results[0]

    return {
        "reply": reply,
        "tokensUsed": 120,
        "retrievedChunks": len(results)
    }