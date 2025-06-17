from fastapi import FastAPI

app = FastAPI()

@app.get("/api/greeting")
def get_greeting(name: str = "FastAPI!"):
    return {"message": f"Hello from {name}"}
