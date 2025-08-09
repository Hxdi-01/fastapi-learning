# Topics:

# Dependency Injection -Your AI agent will need to reuse things ---Depends
# Middleware                                                    ---Request
# Background Tasks                                              ---BackgroundTasks
from fastapi import FastAPI, Request, BackgroundTasks, Depends
from pydantic import BaseModel

app = FastAPI()

# Middleware: log every request
@app.middleware("http")
async def log_req(request: Request, call_next):
    print(f"📥 {request.method} {request.url.path}")
    response = await call_next(request)
    print("📤 Response sent")
    return response

# Dependency Injection: dummy API key
def get_api_key():
    return "mock-key-786"

# Background function: saves to log
def save(msg: dict):
    with open("log.txt", "a") as f:
        f.write(str(msg) + "\n")

# Model
class Message(BaseModel):
    text: str

# Routes
@app.get("/agent")
def get_agent(key: str = Depends(get_api_key)):
    return {"key": key}

@app.post("/chat")
def chat(msg: Message, bt: BackgroundTasks, key: str = Depends(get_api_key)):
    bt.add_task(save, {"msg": msg.dict(), "key": key})
    return {"ok": True}





# Extra:
#1 


#2
# 🧠 TL;DR — What’s Happening?
# User makes a request → /agent
# This middleware runs before the route
# logs the method/path
# call_next(request) runs your route function
# Middleware resumes after the route
# logs that the response is ready
# Response is returned to the user

# Imagine this:
# Middleware is like a security guard
# call_next(request) means:
# 🛂 “Okay, this visitor checks out. Let them into the building."

#3