def f_name():
    name = input("what is your name? ")
    last_name = input("what is your last name? ")
    age = input("how old are you? ")
    print(f"insert into registery (name,last_name,age) values('{name}','{last_name}',{age});")


f_name()