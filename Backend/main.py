from fastapi import FastAPI, HTTPException
from typing import List
from schemas import user as user_schema
from models import user as user_model

app = FastAPI()

# 🎨 Endpoint สำหรับ Insert User
@app.post("/users/", response_model=user_schema.User)
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
@app.get("/users/", response_model=List[user_schema.User])
def read_users():
    users = user_model.get_users()
    return users

# 🎨 Endpoint สำหรับ Get User โดยใช้ user_id
@app.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
