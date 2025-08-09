from fastapi import FastAPI


app = FastAPI()


@app.get("/greet/{name}/{lang}") #  Path Parameters
def greet_name(name: str, lang : str):
    if lang == "urdu":
        return {"message": f"Assalamualaikum, {name}!"}
    elif lang == "english":
        return {"message":f"Hello, {name}"}
    else:
        return {"message" : "Unknown language"}
    
@app.get("/profile/{username}") # Path Parameters
def rovalio(username :str):
    return {"message" : f"Welcome to {username}'s profile!"}

@app.get("/math/add/{a}/{b}") #  Path Parameters
def add (a: int, b: int):
    return { "message" : {
                  "a" : a,
                  "b" : b,
                  "result" : a+b} }

@app.get ("/weather") # Query Parameters
def get_weather(city: str):
    return {"message": f"The weather in {city} is sunny."}    