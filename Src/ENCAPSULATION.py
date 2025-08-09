# class Student_grade:
#     def __init__(self, grade):
#         self.__grade = grade
        
#     def get_grade(self):
#         return self.__grade
    
#     def set_grade(self, grade):
#         if   grade < 0 or grade > 100:
#             return "Your grade isn't acceptable"
#         self.__grade = grade
# student = Student_grade(100)
# student.set_grade(1000)
# print(student.get_grade())







# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.__pages = pages
#     def get_pages(self):
#         return self.__pages
#     def set_pages(self, pages):
#         if pages <1 or pages >10000:
#             print("Invalid number of pages!")
#         else:
#             self.__pages = pages
            
#     def is_longbook(self):
#         if self.__pages > 500:
#             return True
#         else:
#             return False
        
#     def __str__(self):
#         return f"{self.title} has {self.__pages} pages!"

# book = Book("48 Laws of power", 666)
# book.set_pages(99999)
# print(book)
# print(book.is_longbook())




# class Library:
#     location = "Main Street"
    
#     def __init__(self, name, book_count):
#         self.name = name
#         self.book_count = book_count
#     def describe(self):
#         return f"Library {self.name} at {self.location} has {self.book_count} books"

# LS = Library("Sindh", 567)
# print(LS.describe())
# LS.location = "Karachi"
# print(LS.describe())

class Readable:
    def read(self):
        return "Reading content"

class Writable:
    def write(self):
        return "Writing content"

class File(Readable, Writable):             #Multiple Inheritance
    pass

f = File()
print(f.read())
print(f.write())


print(isinstance(f, Readable))
print(isinstance(f, File))
print(issubclass(File, Writable))
print(issubclass(File, tuple))
