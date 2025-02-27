from fastapi import FastAPI, Depends, HTTPException  # FastAPI และ Dependency Injection > FastAPI: สร้าง Instance สำหรับ API , Depends: ใช้ Dependency Injection สำหรับเชื่อมต่อ Database 
from sqlalchemy.orm import Session # สร้าง Session เชื่อมต่อกับ Database >  Session: ใช้สร้าง Session เพื่อ Query ข้อมูลจาก Database
from database import SessionLocal, engine # Import จาก database.py
from models import user as models # Import Model จาก models/user.py
from schemas import user as schemas # Import Schema จาก schemas/user.py

# 📦 สร้าง Table หากยังไม่มี
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 🚀 Dependency: สร้าง Session สำหรับแต่ละ Request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📊 Route: ดึงข้อมูลผู้ใช้ทั้งหมด
@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# 📊 Route: ดึงข้อมูลผู้ใช้ตาม ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

'''
🔄 ลำดับการทำงาน:
main.py เรียก get_db() เพื่อสร้าง Session สำหรับแต่ละ Request
get_db() จะเชื่อมต่อกับ MySQL ผ่าน SessionLocal ที่มาจาก database.py
models.User จะถูกเรียกเพื่อ Query ข้อมูลใน read_users() และ read_user()
schemas.User จะจัดรูปแบบข้อมูลก่อน Response
FastAPI ส่ง Response ในรูปแบบ JSON
'''