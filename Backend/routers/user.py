# routers/user.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import user as user_schema
from models import user as user_model

# 📦 สร้าง Router สำหรับ User
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# 🎨 Endpoint สำหรับ Insert User
@router.post("/", response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: user_schema.UserCreate):
    # 🔍 ตรวจสอบ Email ซ้ำ
    existing_users = user_model.get_users()
    for u in existing_users:
        if u['email'] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    # 💾 Insert ข้อมูลและ Return User ที่เพิ่งสร้าง
    new_user = user_model.create_user(user)
    return new_user  # 🔥 Return User ที่มีครบทุก Field


# 🎨 Endpoint สำหรับ Get Users ทั้งหมด
@router.get("/", response_model=List[user_schema.UserResponse])
def read_users():
    users = user_model.get_users()
    return users


# 🎨 Endpoint สำหรับ Get User โดยใช้ user_id
@router.get("/{user_id}", response_model=user_schema.UserResponse)
def read_user(user_id: int):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
