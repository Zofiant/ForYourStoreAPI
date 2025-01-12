from pydantic import BaseModel, EmailStr

class SUserRegister(BaseModel):
    name: str 
    surname:str
    email: EmailStr
    password: str


class SUserAuth(BaseModel):
    email:EmailStr
    password:str