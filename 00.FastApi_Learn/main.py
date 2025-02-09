from fastapi import (FastAPI,
                     HTTPException)
import uvicorn
from pydantic import (BaseModel,
                      Field,
                      EmailStr,
                      ConfigDict)

app = FastAPI()

'''____________________________________________'''

data = {
    'email': 'hello_to_you@email.ru',
    'bio': 'I am cake',
    'age': 12,

}


data_wo_age = {
    'email': 'hello_to_you@email.ru',
    'bio': 'I am a cake',
    # 'gender': 'male',
    # 'birthday': '2022',
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str = Field(None, max_length=10)



class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra = 'forbid')


# user_1 = UserAgeSchema(**data)
user_2 = UserSchema(**data)
# print(repr(user_1))
print(repr(user_2))

users = []

@app.post('/users')
def add_user(user: UserSchema):
    users.append(user_2)
    return{'ok': True, 'msg': 'User added'}

@app.get('/users')
def get_user():
    return users



























'''____________________________________________'''
#
# books = [
#     {
#         "id": 1,
#      "title": "Преступление и наказание",
#      "author": "Фёдор Достоевский"
#     },
#     {
#         "id": 2,
#      "title": "Мастер и Маргарита",
#      "author": "Михаил Булгаков"
#     }
# ]
#
# @app.get('/books',
#          tags=['Books 📚'],
#          summary='Receive all books')
# def read_books():
#     return books
#
# @app.get('/books/{book_id}',
#          tags=['Books 📚'],
#          summary='Receive some book')
# def get_book(book_id: int):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book is None:
#         raise HTTPException(
#             status_code=404,
#             detail='Book is not found')
#     return book
#
# class NewBook(BaseModel):
#     title: str
#     author: str
#
# @app.post('/books',
#           tags=['Books 📚'],
#           summary='Add some book')
# def create_book(new_book: NewBook):
#     new_entry = {
#         "id": len(books) + 1,
#         "title": new_book.title,
#         "author": new_book.author}
#     books.append(new_entry)
#     return {
#         'success': True,
#         'message': 'Book added'}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)