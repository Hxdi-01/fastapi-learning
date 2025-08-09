# DAY 8: Learn HTTP methods: GET, POST, PUT, DELETE. Test in Postman
# POST = “Here’s new data, figure out where to put it.”
# PUT = “Update what’s at this specific place.”

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: int

books = {}

@app.get("/books")
def get_books():
    return books

@app.post("/books/{book_id}")
def add_book(book_id: int, book: Book):
    if book_id in books:
        return {"message": "The book with same ID already exists!"}
    books[book_id] = book
    return {"message": "The book has been added successfully!", "book": book}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    if book_id not in books:
        return {"message": "No book Found!"}
    books[book_id] = updated_book
    return {"message": "Book Updated Successfully!", "book": updated_book}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        return {"error": "Book not found"}
    del books[book_id]
    return {"message": f"Book with ID {book_id} has been deleted"}
