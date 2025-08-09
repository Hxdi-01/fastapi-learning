class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Wolf(Animal):
    def speak(self):
        return "Howl"
    
pets = [Dog(), Cat(), Wolf(), Animal()]

for pet in pets:
    print(pet.speak())
    
    #Memorize this summary:

# Inheritance = one class gets code from another.

# Multiple Inheritance = inherits from more than one class.

# Polymorphism = same method name, different behavior in each class.

# isinstance / issubclass = type checking.