import pymysql.cursors

# 🔗 การเชื่อมต่อกับ MySQL
def get_connection():
    connection = pymysql.connect(
        host='host.docker.internal',
        user='root',
        password='1111',
        database='nor_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
