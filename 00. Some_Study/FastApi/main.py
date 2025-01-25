from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books= [
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell"
  }
]

@app.get(
    '/books',
    tags = ['books'],
    summary="Get all books"
         )
def get_books():
    return books

@app.get(
    '/books/{book_id}',
    tags=['books'],
    summary="Get a book by ID"
         )
def read_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

class NewBook(BaseModel):
    title: str
    author: str

@app.post('/books', tags=['books'], summary="Create a new book")
def create_book(new_book: NewBook):
    book = {
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    }
    books.append(book)
    return {'success': True, 'data': book, 'message': 'Book created successfully'}
















if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
