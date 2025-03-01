# main.py
from fastapi import FastAPI
from routers import user as user_router
from fastapi.middleware.cors import CORSMiddleware


# 🚀 สร้าง FastAPI App
app = FastAPI(
    title="User Management API",
    description="API สำหรับจัดการ User เช่น สร้าง, ดู, ลบ, แก้ไข",
    version="1.0.0"
)

# 🔗 รวม Router เข้ากับ FastAPI App
app.include_router(user_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # สามารถเปลี่ยนเป็น ["http://localhost:5500"] ตาม Origin ของ Frontend ได้
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)