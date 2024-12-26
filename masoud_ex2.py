#def f_create_list():
 #   file = open("registeration_file.txt", "x")
#f_create_list()

def f_read_list():
    f = open("registeration_file.txt", "r")
    print(f.read())
f_read_list()

def f_name():
    i=1
    while i<=2:
        name=input("what is your name? ")
        last_name=input("what is your last name? ")
        age=input("how old are you? ")
        i=i+1
        f = open("registeration_file.txt", "a")
        f.write(name +"\t"+ last_name+"\t"+age+"\n")

f_name()