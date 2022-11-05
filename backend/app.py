from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

host = os.getenv("CORS_HOST")
print("Host we are working with: " + str(host))

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "http://" + str(host)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Python backend interface"}


@app.get("/contact")
async def contact_backend():
    return {"success":"Hello from backend!"}
