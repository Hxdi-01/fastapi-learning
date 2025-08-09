# class Person: 
#     #attributes
    
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     #method
#     def introduce(self):
#         print(f"Hi I'm {self.name} and I'm {self.age} years old and I study in grade {self.grade}.")
# student = Person("Hxdi", 16, "10th")
# student.introduce()

# class Counter:
#     def __init__(self):
#         self.count = 0
        
#     def increment(self):
#         self.count +=1
        
#     def get(self):
#         return self.count
    
# counter = Counter()

# print(counter.get()) 
# for _ in range(5):
#     counter.increment()
#     print(counter.get())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year
    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"
my_car = Car("Toyota", "Supra", 2012)
print(my_car.get_info())

class Electric(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
       
        self.battery_size = battery_size
        
    def get_info(self):
        return f"{super().get_info()} - Battery: {self.battery_size} "
my_electric = Electric("Tesla", "Model S", 2021, "85 kWh")
print(my_electric.get_info())
    