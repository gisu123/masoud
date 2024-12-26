import mysql.connector
import pandas as pd


def db_connect():
    db_conn = mysql.connector.connect(
      host="localhost",
      user="python",
      password="python123",
      database="sakila"
    )

    return db_conn



def f_fetch_data_merged():
    mydb_conn =db_connect()
    mycursor1 = mydb_conn.cursor()
    mycursor1.execute("select * from film ")
    table1 = mycursor1.fetchall()
    column_names1 = [x[0] for x in mycursor1.description]
    mycursor2 = mydb_conn.cursor()
    mycursor2.execute("select * from film_actor")
    table2 = mycursor2.fetchall()
    column_names2 = [x[0] for x in mycursor2.description]
    df1 = pd.DataFrame(data=table1, columns=column_names1)
    df2 = pd.DataFrame(data=table2, columns=column_names2)
    result = pd.merge(df1,df2,on="film_id")
    result.to_csv("merge_file.csv")


f_fetch_data_merged()



