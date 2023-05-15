from typing import List, Optional
from pydantic import BaseModel

#Login 
class UserCreate(BaseModel):
    user_email : str
    user_password : str

#Signin
class User(BaseModel):
    user_email : str
    user_password : str

