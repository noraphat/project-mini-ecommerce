import pymysql.cursors
#Windows host='host.docker.internal',
#Mac host='localhost',
# 🔗 การเชื่อมต่อกับ MySQL
def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1111',
        database='nor_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
