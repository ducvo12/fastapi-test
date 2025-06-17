from main import FastAPI

app = FastAPI()

@app.get("/api/greeting")
def get_greeting(name: str = "FastAPI!"):
    return {"message": f"Hello from {name}"}

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}