import mysql.connector as mysql

config = dict(host='localhost',
              user='python',
              password='python123',
              database='python')

my_connection = mysql.connect(**config)
cur = my_connection.cursor()
cur.execute('select * from registery')
result = cur.fetchall()
print(result)
