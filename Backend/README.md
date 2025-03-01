# 🚀 คู่มือการติดตั้งโปรเจกต์ FastAPI

## 🔧 Project Setup

1️⃣ Clone the Repository

# Clone this repository
$ git clone <repository_url>
git clone https://github.com/noraphat/project-mini-ecommerce.git


$ cd <repository_folder>
cd project-mini-ecommerce\Backend


## 📂 โครงสร้างโปรเจกต์
```
project-mini-ecommerce/
├── Backend/
│   ├── models/
│   │   ├── user.py
│   ├── routers/
│   │   ├── user.py
│   ├── schemas/
│   │   ├── user.py
│   ├── database.py
│   ├── main.py
│   ├── requirements.txt
│
├── Frontend/
```

## 🛠️ การติดตั้ง Dependencies
### Windows
```bash
python -m venv venv  # สร้าง virtual environment
venv\Scripts\activate  # เปิดใช้งาน venv
pip install -r requirements.txt  # ติดตั้ง dependencies
```

### MacOS/Linux
```bash
python3 -m venv venv  # สร้าง virtual environment
source venv/bin/activate  # เปิดใช้งาน venv
pip3 install -r requirements.txt  # ติดตั้ง dependencies
```

---

## 🐳 การตั้งค่า Docker
### 1️⃣ สร้าง Docker Network
```bash
docker network create nw_20250315_database
```

### 2️⃣ รัน Container ของ MySQL
```bash
docker run --name db_mysql -e MYSQL_ROOT_PASSWORD=1111 --network nw_20250315_database -p 3306:3306 -d mysql:5.7
```

### 3️⃣ รัน phpMyAdmin (ตัวเลือกเสริม)
```bash
docker run --name db_phpmyadmin --network nw_20250315_database -p 8888:80 -e PMA_ARBITRARY=1 -d phpmyadmin/phpmyadmin
```

### 4️⃣ เข้าใช้งาน phpMyAdmin
- เปิดเบราว์เซอร์: [http://localhost:8888](http://localhost:8888)
- Server: `db_mysql`
- Username: `root`
- Password: `1111`

---

## 🛠️ การตั้งค่าฐานข้อมูล
### 5️⃣ เข้าถึง MySQL และสร้างฐานข้อมูล
#### เชื่อมต่อผ่าน CLI:
```bash
docker exec -it db_mysql mysql -u root -p
```
#### รันคำสั่ง SQL:
```sql
CREATE DATABASE nor_db;
USE nor_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    address TEXT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (first_name, last_name, email, phone, address, username, password, created_at) VALUES
('John', 'Doe', 'john.doe@email.com', '0812345678', '123 Main St, Bangkok', 'user1', '12345678', NOW()),
('Alice', 'Smith', 'alice.smith@email.com', '0898765432', '456 Central Rd, Chiang Mai', 'user2', '12345678', NOW());
```

---

## 🚀 การรันเซิร์ฟเวอร์ FastAPI
### 6️⃣ เริ่มต้นเซิร์ฟเวอร์ FastAPI
#### Windows:
```bash
uvicorn main:app --reload
```
#### MacOS/Linux:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🔥 API Endpoints
### 📌 Base URL: `http://127.0.0.1:8000`
| Method   | Endpoint      | คำอธิบาย |
| -------- | ------------- | -------- |
| `GET`    | `/users/`     | ดึงข้อมูลผู้ใช้ทั้งหมด |
| `GET`    | `/users/{id}` | ดึงข้อมูลผู้ใช้ตาม ID |
| `POST`   | `/users/`     | เพิ่มผู้ใช้ใหม่ |
| `PUT`    | `/users/{id}` | อัปเดตข้อมูลผู้ใช้ |
| `DELETE` | `/users/{id}` | ลบผู้ใช้ |

---

## 🛠️ ทดสอบ API ด้วย Postman
### 7️⃣ ใช้งาน Postman เพื่อลอง API
1. เปิด **Postman**
2. สร้าง **Request ใหม่**
3. เลือก **Method** (GET, POST, PUT, DELETE)
4. ใส่ **URL** (`http://127.0.0.1:8000/users/`)
5. ใช้ **Body** (สำหรับ POST & PUT) ในรูปแบบ `JSON`

ตัวอย่าง Body สำหรับ POST:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@email.com",
  "phone": "0812345678",
  "address": "123 Main St",
  "username": "john123",
  "password": "securepassword"
}
```

## ✅ เสร็จสิ้น! 🎉
ตอนนี้คุณสามารถทดสอบ API ผ่าน **Postman** หรือ **Swagger UI** ที่ `http://127.0.0.1:8000/docs` 🚀
