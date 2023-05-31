from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    user_name: str
    user_last_name: str
    user_rol: str
    user_pricing_plan: str
    user_username: str
    user_email: str
    user_password: str
    user_profile_img_url: str
    user_loged: Optional[bool]

    class Config:
        orm_mode = True


#Login 
class UserCreate(BaseModel):
    user_email : str
    user_password : str

#Signin
class SignedUser(BaseModel):
    user_email : str
    user_password : str


class UpdatedUser(BaseModel):
    user_email: str
    user_loged: bool = False


class DeletedUser(BaseModel):
    id: int
    


    


