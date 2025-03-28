from fastapi import (FastAPI,
                     HTTPException)
import uvicorn
from pydantic import (BaseModel,
                      Field,
                      EmailStr,
                      ConfigDict)

app = FastAPI()
books = [
    {
        "id": 1,
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский"
    },
    {
        "id": 2,
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков"
    }
]


@app.get('/books',
         tags=['Books 📚'],
         summary='Receive all books')
def read_books():
    return books


@app.get('/books/{book_id}',
         tags=['Books 📚'],
         summary='Receive some book')
def get_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        raise HTTPException(
            status_code=404,
            detail='Book is not found')
    return book


class NewBook(BaseModel):
    title: str
    author: str


@app.post('/books',
          tags=['Books 📚'],
          summary='Add some book')
def create_book(new_book: NewBook):
    new_entry = {
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author}
    books.append(new_entry)
    return {
        'success': True,
        'message': 'Book added'}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
