import mysql.connector
import pandas as pd


def db_connect():
    db_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="NedaSQL!",
      database="world"
    )

    return db_conn

def f_new_population(row):
    return row["population"]+2000000

def f_fetch_data_apply_changes():
    mydb_conn =db_connect()
    mycursor = mydb_conn.cursor()
    mycursor.execute("select name,continent,population from country ")
    table = mycursor.fetchall()
    column_names = [x[0] for x in mycursor.description]

    df = pd.DataFrame(data=table, columns=column_names)
    df["updated_population"] = df.apply(f_new_population, axis=1)
    df.to_csv("country_file.csv")


f_fetch_data_apply_changes()


