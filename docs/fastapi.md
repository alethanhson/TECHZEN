# FastAPI & SQLAlchemy v2 & Pydantic v2 Cheat Sheet

## 1. FastAPI Basics
### Basic App & Routing
```python
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

app = FastAPI(title="Techzen API")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

### Dependency Injection
```python
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# In routes:
from sqlalchemy.orm import Session
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    # ... logic
```

## 2. Pydantic v2 (Schemas)
```python
from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserRead(UserBase):
    id: int
    
    # Pydantic v2: Config object replaces class Config
    model_config = ConfigDict(from_attributes=True)
```

## 3. SQLAlchemy v2 (Models)
### Declarative Base & Models
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    
    items: Mapped[list["Item"]] = relationship(back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    owner: Mapped["User"] = relationship(back_populates="items")
```

### CRUD Operations (SQLAlchemy 2.0 style)
```python
from sqlalchemy import select, update, delete

# Select all
stmt = select(User).where(User.is_active == True)
users = db.scalars(stmt).all()

# Select one
user = db.get(User, user_id) 
# or
user = db.scalar(select(User).where(User.id == user_id))

# Create
db_user = User(**user_in.model_dump()) 
db.add(db_user)
db.commit()
db.refresh(db_user)

# Update
stmt = update(User).where(User.id == user_id).values(email="new@example.com")
db.execute(stmt)

# Delete
stmt = delete(User).where(User.id == user_id)
db.execute(stmt)
```

## 4. Error Handling
```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Item not found"
)
```

## 5. Background Tasks
```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(message)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"notification sent to {email}")
    return {"message": "Notification sent in the background"}
```
