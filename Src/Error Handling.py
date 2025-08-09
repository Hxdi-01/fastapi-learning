# Basic structure:
# try:
    # Code that might throw an error
#except SomeError:
    # Code to run if that error happens
    
try: 
   x = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

try:
    lol = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input! Enter a number.")

try:
    fun = int("123")
except ValueError:
    print ("Conversion Unsuccessful.")
else:
    print("Conversion Successful.")
finally:
    print("End of code.")

marks = int(input("Input your marks: "))
try:
    if marks <0:
        raise ValueError("Marks can't be negative!") 
except ValueError as e:
    print(e)
 