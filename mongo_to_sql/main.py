import mysql.connector

def test_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root_password',
            database='dev_db',
            port=3306,
        )
        print("✅ MySQL Connection Successful!")
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")



if '__main__' == __name__:
    test_mysql()