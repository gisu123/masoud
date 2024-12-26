#name=input("what is your name? ")
#last_name=input("what is your last name? ")
#age=input("how old are you? ")
#print("hello "+name+" "+last_name+" "+age+" years old")


#def f_name():
  #  i=1
  #  while i<=2:
   #     name=input("what is your name? ")
  #      last_name=input("what is your last name? ")
 #       age=input("how old are you? ")
  #      i=i+1
  #      print(name +"\t"+ last_name+"\t"+age)
#f_name()



def f_name():
    file = open("registery_file.txt", "x")
    i=1
    while i<=2:
        name=input("what is your name? ")
        last_name=input("what is your last name? ")
        age=input("how old are you? ")
        i=i+1
        file.write(name +"\t"+ last_name+"\t"+age+"\n")

f_name()