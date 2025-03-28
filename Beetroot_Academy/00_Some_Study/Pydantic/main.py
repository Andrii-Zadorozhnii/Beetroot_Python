from pydantic import BaseModel, Field, EmailStr

data = {
     'email': 'abc@gmail',
     'bio': None,
     'age': -12,
 }
class UserSchema(BaseModel):
        email: EmailStr
        bio: str | None
        age: int = Field(ge=0, le=130)

user = UserSchema(**data)

print(user)

