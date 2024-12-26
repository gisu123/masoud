import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="Python123!",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "select f.film_id,f.title,f.description,f.release_year,fa.actor_id from \
film f join film_actor fa on f.film_id=fa.film_id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)