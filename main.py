from fastapi import FASTAPI

app = FASTAPI(title="AI RAG Assistant")

@app.get("/")
def home():
    return {
        "message" : "Welcome to AI RAG Assistant"
        
    }