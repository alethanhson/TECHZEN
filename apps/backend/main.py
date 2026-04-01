from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import os

from . import models, schemas, database
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TECHZEN CRUD API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")

@api_router.get("/health")
def check_health():
    return {"status": "ok"}

@api_router.get("/employees", response_model=List[schemas.Employee])
def get_employees(search: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Employee)
    if search:
        query = query.filter(models.Employee.name.contains(search) | models.Employee.code.contains(search))
    return query.all()

@api_router.get("/employees/{emp_id}", response_model=schemas.Employee)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_emp

@api_router.post("/employees", response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = models.Employee(**emp.model_dump())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

@api_router.put("/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, emp: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    update_data = emp.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_emp, key, value)
    
    db.commit()
    db.refresh(db_emp)
    return db_emp

@api_router.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_emp)
    db.commit()
    return {"message": f"Successfully deleted employee {emp_id}"}

app.include_router(api_router)