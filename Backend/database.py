from sqlalchemy import create_engine # สร้าง Engine สำหรับเชื่อมต่อ Database
from sqlalchemy.ext.declarative import declarative_base # Base สำหรับสร้าง Model
from sqlalchemy.orm import sessionmaker # สร้าง Session สำหรับเชื่อมต่อ Database

# Database URL: เชื่อมต่อกับ MySQL ที่อยู่ใน Docker
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1111@host.docker.internal:3306/nor_db"




# สร้าง Engine และ SessionLocal สำหรับเชื่อมต่อ Database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง Base สำหรับการสร้าง Model
Base = declarative_base()
