# class=blueprint/dummy model/design of an object
# object=intance of a class/physical existence of a class
# syntax of class
# comment execute nhi hota h 

class A:
    "doc string" #idhr doc string ko agr call kra toh execute hojaega
    x=10  #method
    def new():  #var
        print("hello")
obj=A
print(obj.x)
obj.new()
obj1=A
print(obj1.x)
obj1.new()
print(dir(A))#dir shows all the hidden method in the class
print(A. __doc__) #doc calls the msg we have passed in the string