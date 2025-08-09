import json
car_name          =        str(input("Enter the car's name: "))
car_fuel          =        str(input("Fuel types of the car: ")).split(",")
countries         =        str(input("Enter the countries separated by commas: ")).split(",")
car_speed         =        int(input("Max speed of the car: "))

stock = {}
for country in countries:
    qty = int(input(f"Enter stock for {country.strip()}: "))
    stock[country.strip()] = qty

try:
    with open("cars.json", "r") as file:
        all_cars = json.load(file)
except FileNotFoundError:
    all_cars = []
    
new_car = {
    "Car Name"       :  car_name,
    "Car Fuel Type"  :  car_fuel,
    "Car Stock"      :  stock,
    "Car Speed"      :  car_speed}

all_cars.append(new_car)

with open("cars.json", "w") as file:
    json.dump(all_cars, file, indent=2)
    
print("✅ Car saved successfully, Updated car list:")
print(all_cars)
