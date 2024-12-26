import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="python123",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



#Note: We use the fetchall() method, which fetches all rows from the last executed statement.