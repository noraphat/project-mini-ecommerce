from pydantic import BaseModel # สร้าง Schema สำหรับ Request และ Response > BaseModel: ใช้กำหนด Schema เพื่อจัดการกับ Request และ Response
from datetime import datetime # ใช้ในฟิลด์ created_at > datetime: ใช้กำหนดประเภทข้อมูลใน created_at

# ✨ สร้าง Schema สำหรับการแสดงผล
class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    full_name: str  # ดึงค่าจาก Property ใน models/user.py
    email: str
    phone: str | None
    address: str | None
    username: str
    created_at: datetime

    class Config:
        orm_mode = True



'''
🔄 ลำดับการทำงาน:
BaseModel: เป็นแม่แบบในการกำหนด Schema ของ Pydantic
orm_mode = True: ทำให้ Pydantic สามารถรับค่าโดยตรงจาก SQLAlchemy Model
full_name: เป็นฟิลด์ที่ไม่ได้เก็บใน Database แต่สร้างขึ้นจาก @property ใน models/user.py
'''