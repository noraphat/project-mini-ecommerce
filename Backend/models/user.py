from sqlalchemy import Column, Integer, String, Text, DateTime, func  # สร้าง Column ของ Table ฬ ใช้สร้าง Column ที่แมพกับฟิลด์ใน MySQL
from database import Base # Import Base จาก database.py > เพื่อใช้เป็น Class แม่ในการสร้าง Model

# 📦 สร้าง Model สำหรับ Table Users
class User(Base):
    __tablename__ = "users" # 🔖 ชื่อตารางใน MySQL

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=True)
    address = Column(Text, nullable=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # สร้าง full_name โดยใช้ Property (ไม่ได้เก็บใน Database)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"