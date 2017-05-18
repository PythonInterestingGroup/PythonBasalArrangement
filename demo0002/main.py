import string
import random
import mysql.connector

def randomCodes():
    conn = mysql.connector.connect(user='root', password='486904', database='python_demo')
    cursor = conn.cursor()
    chars = string.ascii_letters + string.digits
    for i in range(200):
        code = ''.join([random.choice(chars) for i in range(32)])
        cursor.execute('insert into random_codes (code) values (%s)', [code])
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    randomCodes()
