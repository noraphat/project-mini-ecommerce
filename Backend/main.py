# main.py
from fastapi import FastAPI
from routers import user as user_router

# 🚀 สร้าง FastAPI App
app = FastAPI(
    title="User Management API",
    description="API สำหรับจัดการ User เช่น สร้าง, ดู, ลบ, แก้ไข",
    version="1.0.0"
)

# 🔗 รวม Router เข้ากับ FastAPI App
app.include_router(user_router.router)
