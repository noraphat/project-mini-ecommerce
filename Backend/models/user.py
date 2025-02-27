from database import get_connection

# 🚀 Query สำหรับ Insert User และ Return User ที่เพิ่ง Insert
def create_user(user):
    conn = get_connection()
    with conn.cursor() as cursor:
        # 💾 Insert User
        sql = """
            INSERT INTO users (first_name, last_name, email, phone, address, username, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            user.first_name,
            user.last_name,
            user.email,
            user.phone,
            user.address,
            user.username,
            user.password
        ))
        conn.commit()
        
        # 🔍 ดึงข้อมูล User ที่เพิ่ง Insert มาเพื่อตอบกลับ
        user_id = cursor.lastrowid  # ได้ `user_id` ที่เพิ่ง Insert
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        new_user = cursor.fetchone()
        
        # 🎨 สร้าง full_name ก่อน Return
        new_user['full_name'] = f"{new_user['first_name']} {new_user['last_name']}"

    conn.close()
    return new_user  # 🔥 Return ครบทุก Field


# 🚀 Query สำหรับ Select Users ทั้งหมด
def get_users():
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        users = cursor.fetchall()
    conn.close()
    return users

# 🚀 Query สำหรับ Select User โดยใช้ user_id
def get_user_by_id(user_id: int):
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()
        
        # 🔥 คำนวณ full_name ในระดับ Model
        if user:
            user['full_name'] = f"{user['first_name']} {user['last_name']}"

    conn.close()
    return user

