from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/chat")
def uppercase(message: str):
    return {"message" :  message.upper() }

@app.post ("/webhook")
async def recieve_webhook(request : Request):
    data = await request.json()
    print("📦 Incoming Webhook Data:", data)
    return {"status" : "Webhook recieved"}