# Day 9: Learn headers, payload, status codes + how JSON moves in & out

from fastapi import FastAPI, Header, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. JSON payload model
class User(BaseModel):
    username: str
    email: str

# 2. POST /register endpoint
@app.post("/register")
def register_user(
    user: User,
    x_api_key: Optional[str] = Header(None)  # Reading header
):
    if x_api_key != "supersecret":
        return {
            "status": "error",
            "message": "Invalid or missing API Key"
        }, status.HTTP_401_UNAUTHORIZED  # custom status code

    return {
        "status": "success",
        "message": f"User {user.username} registered successfully",
        "data": user
    }

# 3. Echo endpoint (for testing JSON in/out)
@app.post("/echo")
def echo_json(data: dict):
    return {"you_sent": data}

# 4. GET /headers endpoint (for seeing all request headers)
@app.get("/headers")
def read_headers(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}
