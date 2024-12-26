import mysql.connector
import csv

# def f_create_file():
#     file = open("db_file.csv", "x")
#
#
# f_create_file()


def data_to_csv(result):
    with open('db_file.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)


def db_connect():
    mydb_conn = mysql.connector.connect(
      host="localhost",
      user="python",
      password="python123",
      database="sakila"
    )

    return mydb_conn

def f_fetch_data():
    mydb_conn =db_connect()
    mycursor = mydb_conn.cursor()
    mycursor.execute("SELECT * FROM actor")
    result = mycursor.fetchall()
    data_to_csv(result)


f_fetch_data()








