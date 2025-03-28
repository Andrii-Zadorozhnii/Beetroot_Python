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
def get_user() -> list[UserSchema]:
    return users



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)