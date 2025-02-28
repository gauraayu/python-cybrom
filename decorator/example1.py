# used for security purposes
# it is special type of higher order functn
# it is a type of higher order functn jo ek fucntn as a argument leta h aur functn hi return krta h 
# inner functn ka behaviour bina chnge kre op chnge krna
# agr 2+3 5 nhi aur 10 dena h toh decorator use krte for example
# @ symbol is used in decorator
def outer_fun(new):
    def inner_fun():
        print("hello")
    return inner_fun
@outer_fun
def new():
    pass
    #  print("hi")
#op empty ana chahie pr hello arha decorator ki vjh s
new()
