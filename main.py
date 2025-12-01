from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, get_db
from sqlalchemy.orm import Session
import models, schemas
from utils import hash_password, verify_password
from auth import create_token
 
app = FastAPI()
 
Base.metadata.create_all(bind=engine)
 
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_exist = db.query(models.User).filter(models.User.username == user.username).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="User already exists")
 
    hashed = hash_password(user.password)
    new_user = models.User(username=user.username, email=user.email, password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}
 
@app.post("/login")
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == data.username).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
 
    token = create_token({"username": user.username})
    return {"access_token": token, "token_type": "bearer"}
 
from schemas import StaffCreate, StaffResponse
import models
from fastapi import Depends
from sqlalchemy.orm import Session
 
# Add Staff
@app.post("/staff/add", response_model=StaffResponse)
def add_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    new_staff = models.Staff(name=staff.name, role=staff.role, contact=staff.contact)
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff
 
# Get All Staff
@app.get("/staff/all")
def get_all_staff(db: Session = Depends(get_db)):
    staff_list = db.query(models.Staff).all()
    return staff_list
 
# Update Staff
@app.put("/staff/update/{id}")
def update_staff(id: int, staff: StaffCreate, db: Session = Depends(get_db)):
    staff_data = db.query(models.Staff).filter(models.Staff.id == id).first()
    if not staff_data:
        return {"error": "Staff not found"}
 
    staff_data.name = staff.name
    staff_data.role = staff.role
    staff_data.contact = staff.contact
    db.commit()
    return {"message": "Staff updated successfully"}
 
# Delete Staff
@app.delete("/staff/delete/{id}")
def delete_staff(id: int, db: Session = Depends(get_db)):
    staff_data = db.query(models.Staff).filter(models.Staff.id == id).first()
    if not staff_data:
        return {"error": "Staff not found"}
 
    db.delete(staff_data)
    db.commit()
    return {"message": "Staff deleted successfully"}