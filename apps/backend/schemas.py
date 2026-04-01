from pydantic import BaseModel
from typing import Optional

# Base Schema (Định nghĩa các trường chung)
class EmployeeBase(BaseModel):
    code: str
    name: str
    type: Optional[str] = "User"
    note: Optional[str] = None
    active: Optional[bool] = True

# Schema để nhận dữ liệu từ FE khi tạo mới
class EmployeeCreate(EmployeeBase):
    pass

# Schema dùng để Update
class EmployeeUpdate(EmployeeBase):
    name: Optional[str] = None
    code: Optional[str] = None

# Schema dùng khi trả dữ liệu về FE (có thêm ID)
class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
