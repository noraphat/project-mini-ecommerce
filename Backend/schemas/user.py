from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from datetime import datetime

# 🎨 Schema สำหรับสร้าง User
class UserCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: Optional[str] = Field(None, pattern="^0[0-9]{9}$")  # เบอร์โทรไทย 10 หลัก
    address: Optional[str]
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)

    # ✨ Custom Validation: เช็คว่าชื่อห้ามเป็น "admin"
    @field_validator('username')
    def username_must_not_be_admin(cls, v):
        if v.lower() == 'admin':
            raise ValueError('Username cannot be "admin"')
        return v

# 🎨 Schema สำหรับการแสดงผล User
class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    full_name: str
    email: str
    phone: Optional[str] = Field(None, pattern="^0[0-9]{9}$")  # เบอร์โทรไทย 10 หลัก
    address: Optional[str]
    username: str
    created_at: datetime

    class Config:
        orm_mode = True
