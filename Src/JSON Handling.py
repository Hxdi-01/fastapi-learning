# Important:
# loads() → reading the instructions and building the toy.

# dumps() → taking your toy and writing the instructions.

# load() → reading instructions from a file.

# dump() → saving instructions to a file.




import json

# JSON str To Python-----------------------------------------------------------------------------------------------
# {
    
#     "brand": "Nike",
#     "Size": 42,
#     "Color": ["black","white"]
    
# }

# json_note= '{ "brand" : "Nike", "size" : 42, "color" : ["black","white"]}'
# shoes = json.loads(json_note)

# print(shoes["brand"])
# print(shoes["color"])


# Writing JSON (From Python to JSON) ----------------------------------------------------------------------------

import json

person = {
    "name": "Hadi",
    "age": 16,
    "skills": ["marketing", "python"]
}
json_data = json.dumps(person)
print(json_data)

# Saving JSON to a File-------------------------------------------------------------------------------------------

with open("data.json", "w") as file:
    json.dump(person, file)

#Reading JSON from a File------------------------------------------------------------------------------------------

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])



