from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/api/greeting")
def get_greeting(name: str = "FastAPI!"):
    return {"message": f"Hello from {name}"}

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}