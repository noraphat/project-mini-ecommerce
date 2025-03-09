import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

# 🔒 กำหนดค่าความปลอดภัยของ JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # อายุของ Token (30 นาที)

# ใช้ bcrypt สำหรับ Hash Password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str):
    """ 🔒 แปลงรหัสผ่านเป็น Hash ก่อนบันทึก """
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """ 🔍 ตรวจสอบรหัสผ่านที่ผู้ใช้กรอกกับ Hash ในฐานข้อมูล """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    """ 🔥 สร้าง JWT Token """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """ 🧐 ตรวจสอบ JWT Token """
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """ ✅ ดึงข้อมูล User จาก JWT Token """
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload
