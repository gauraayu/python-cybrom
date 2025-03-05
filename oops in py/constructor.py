#special type of method that calls itself
class S:
    def __init__(self):
        print("hi")
    def display(self):
        print("hello")
# obj=S    #show error
# obj.display()    
obj=S()   
obj.display()
print(id(obj))
