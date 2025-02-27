from database import get_connection

# 🚀 Query สำหรับ Insert User
def create_user(user):
    conn = get_connection()
    with conn.cursor() as cursor:
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
    conn.close()

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

