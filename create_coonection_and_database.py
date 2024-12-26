
#Create Connection
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="python123"
)

print(mydb)

#Creating a Database
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Python")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)