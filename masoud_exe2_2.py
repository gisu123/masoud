#def f_create_list():
#    file = open("regis_file.txt", "x")
#f_create_list()

def f_read_list():
    f = open("regis_file.txt", "r")
    print(f.read())
f_read_list()

def f_name():
        name=input("what is your name? ")
        last_name=input("what is your last name? ")
        age=input("how old are you? ")
        f = open("regis_file.txt", "a")
        f.write(name +"\t"+ last_name+"\t"+age+"\n")

f_name()