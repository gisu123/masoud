from masoud_sql_queries import insert_query


def f_name():
    name = input("what is your name? ")
    last_name = input("what is your last name? ")
    age = input("how old are you? ")
    print(insert_query.format(name=name, last_name=last_name, age=age))


f_name()