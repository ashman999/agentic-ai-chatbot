from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import run_customer_support  # Import your function from the notebook

app = FastAPI()

# Allow your frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input data model
class ChatRequest(BaseModel):
    message: str

# Response endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    result = run_customer_support(req.message)
    return { "response": result["response"] }


