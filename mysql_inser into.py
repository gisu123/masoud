import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="python123",
  database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


#Important!: Notice the statement: mydb.commit(). It is required to make the changes,
# otherwise no changes are made to the table.

