from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Post_data(BaseModel):
    title: str
    content: str
    published: bool = True

class Post_create(Post_data):
    pass



class Create_user(BaseModel):
    email: EmailStr
    password: str

class User_response(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    # user_id : int
    owner: User_response

    class Config:
        orm_mode = True

class Login_data(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type: str

class Token_data(BaseModel):
    id: Optional[str] 
    
class Answer(BaseModel):
    answer: bool
    