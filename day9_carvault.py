from fastapi import FastAPI, Header, status, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory "database"
cars_db = []
car_counter = 1

# Data model for incoming car info
class Car(BaseModel):
    brand: str
    year: str


# Add a car (requires API key in header)
@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_car(
    car: Car,
    x_api_key: Optional[str] = Header(None)
):
    global car_counter  # let Python know we mean the outer variable

    if x_api_key != "supersecret":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    car_entry = car.dict()
    car_entry["id"] = car_counter
    cars_db.append(car_entry)
    car_counter += 1

    return {
        "status": "success",
        "message": f"Car {car.brand} registered successfully",
        "car": car_entry
    }


# Get all cars
@app.get("/cars", status_code=status.HTTP_200_OK)
def get_cars():
    return {
        "status": "success",
        "cars": cars_db
    }


# Get one car by ID
@app.get("/cars/{car_id}", status_code=status.HTTP_200_OK)
def get_car_by_id(car_id: int):
    for car in cars_db:
        if car["id"] == car_id:
            return {
                "status": "success",
                "car": car
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Car with ID {car_id} not found"
    )


# Delete a car by ID (requires API key)
@app.delete("/cars/{car_id}", status_code=status.HTTP_200_OK)
def delete_car(car_id: int, x_api_key: Optional[str] = Header(None)):
    if x_api_key != "supersecret":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    for car in cars_db:
        if car["id"] == car_id:
            cars_db.remove(car)
            return {
                "status": "success",
                "message": f"Car with ID {car_id} deleted"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Car with ID {car_id} not found"
    )


# Echo JSON payload back to the user
@app.post("/echo", status_code=status.HTTP_201_CREATED)
def echo_json(data: dict):
    return {"you_sent": data}


# Read request headers (built-in + custom)
@app.get("/headers")
def read_headers(
    user_agent: Optional[str] = Header(None),
    x_client_name: Optional[str] = Header(None)
):
    return {
        "User-Agent": user_agent,
        "X-Client-Name": x_client_name
    }
