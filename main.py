from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET route with query param
@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}

# Data model for POST
class LoginData(BaseModel):
    username: str
    password: str

# POST route with body
@app.post("/login")
def login(data: LoginData):
    return {"message": f"Welcome, {data.username}!"}
