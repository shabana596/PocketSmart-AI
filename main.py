from fastapi import FastAPI

app = FastAPI(title="PocketSmart AI")


@app.get("/")
def home():
    return {
        "message": "Welcome to PocketSmart AI!",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
