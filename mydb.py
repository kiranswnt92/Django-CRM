import pymysql

try:
    dataBase = pymysql.connect(
        host='localhost',
        user='root',
        passwd='password123'
    )
    cursorObject = dataBase.cursor()
    cursorObject.execute("CREATE DATABASE elderco")
    print("Database 'elderco' created successfully!")
except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
    if 'dataBase' in locals():
        dataBase.close()
        print("MySQL connection is closed")
