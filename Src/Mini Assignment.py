# # def larger(x,y):
# #     if x < y:
# #         return y
# #     else:
# #         return x

# # print(larger(9, 49))

# # fruits = ["apple", "banana", "mango"]
# # fruits.append ("Orange")
# # print(fruits[1])
# # print(len(fruits))

# # #Tuples
# # Colors = ("red", "green", "blue")
# # print(Colors[2])

# # Book ={
# #     "Title" : "Atomic Habits",
# #     "Author" : "James Clear",
# #     "Year" : 2015
# # }
# # print(Book["Title"])
# # print(Book["Author"])
# # Book["Year"] = 2019
# # print(Book["Year"])

# numbers = [5, 11, 3, 22, 7, 14]
# for num in numbers:
#     if num > 10:
#         print(num)
# import json

# name = str(input("Enter name of the student: ")).strip()
# grade = int(input("Enter the grade of the student: "))
# marks = int(input("Enter the marks obtained: "))

# report_card = {
    
#      "name" : name,
#     "grade" : grade,
#     "marks" : marks, 
# }
   
# with open ("report.json" , "w" ) as file:
#     json.dump(report_card, file)
    
# print("✅ Student data saved!")

# with open ("report.json" , "r") as file:
#     report = json.load(file)
    
# print("📄 Loaded Student Report:")
# print("Name: ", report["name"])
# print("Grade: ", report["grade"])
# print("Marks: ", report["marks"])


# info = {
#     "Brand" : "Tesla",
#     "Car Name" : "Cybertruck",
#     "Color" : "Gray",
#     "Prices" : {
#         "Pakistan" : 20000000,
#         "UAE" : 100000,
#     } ,
#     "Fuel type" : ["Petrol", "Electric"]
# }

# print(info["Brand"])
# print(info["Prices"]["UAE"])
# print(info["Fuel type"][1])

# info["Fuel type"].append ("Diesel")
# print(info["Fuel type"][2])
# info["Prices"]["USA"] = 88000
# print(info["Prices"])

# info["Prices"]["Pakistan"] = 1900000
# print(info["Prices"]["Pakistan"])

# info["Fuel type"][0] = "Plasma"
# print(info["Fuel type"][0])

# for country, cost in info["Prices"].items():
#     print(country, ":", cost)

# for fuel_type in info ["Fuel type"]:
#     print("Fuel Type:", fuel_type)

# del info ["Prices"]["USA"]
# info["Fuel type"].remove("Plasma")
# print(info["Fuel type"])
# print(info ["Prices"])
