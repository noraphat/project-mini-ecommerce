from fastapi import FastAPI, HTTPException, status
from typing import List
from schemas import user as user_schema
from models import user as user_model

app = FastAPI()

# 🎨 CREATE: Endpoint สำหรับ Insert User
@app.post("/users/", response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: user_schema.UserCreate):
    # 🔍 ตรวจสอบ Email ซ้ำ
    existing_users = user_model.get_users()
    for u in existing_users:
        if u['email'] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    # 💾 Insert ข้อมูลและ Return User ที่เพิ่งสร้าง
    new_user = user_model.create_user(user)
    return new_user  # 🔥 Return User ที่มีครบทุก Field


# 🎨 READ: Endpoint สำหรับ Get Users ทั้งหมด
@app.get("/users/", response_model=List[user_schema.UserResponse])
def read_users():
    users = user_model.get_users()
    return users


# 🎨 READ: Endpoint สำหรับ Get User โดยใช้ user_id
@app.get("/users/{user_id}", response_model=user_schema.UserResponse)
def read_user(user_id: int):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 🎨 UPDATE: Endpoint สำหรับ Update User โดยใช้ user_id
@app.put("/users/{user_id}", response_model=user_schema.UserResponse)
def update_user(user_id: int, user: user_schema.UserUpdate):
    # 🔍 ตรวจสอบ User ว่ามีอยู่หรือไม่
    existing_user = user_model.get_user_by_id(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 💾 อัปเดตข้อมูลและ Return User ที่อัปเดตแล้ว
    updated_user = user_model.update_user(user_id, user)
    return updated_user


# 🎨 DELETE: Endpoint สำหรับ Delete User โดยใช้ user_id
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    # 🔍 ตรวจสอบ User ว่ามีอยู่หรือไม่
    existing_user = user_model.get_user_by_id(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 🗑️ ลบข้อมูล
    user_model.delete_user(user_id)
    return {"detail": "User deleted successfully"}
