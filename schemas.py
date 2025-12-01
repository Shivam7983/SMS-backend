from pydantic import BaseModel
 
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
 
class UserLogin(BaseModel):
    username: str
    password: str
 
class StaffCreate(BaseModel):
    name: str
    role: str
    contact: str
 
class StaffResponse(BaseModel):
    id: int
    name: str
    role: str
    contact: str
 
    class Config:
        orm_mode = True
 