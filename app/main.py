from fastapi import FastAPI

app = FastAPI(title="MonArch AI")

@app.get("/")
def root():
    return {"message": "MonArch AI API is running"}
