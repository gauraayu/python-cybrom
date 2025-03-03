def outer_fun(new):
    def inner_fun(p,q):
       p=p+10
       q=q+10
       r=new(p,q)
       print(r)
    return inner_fun
@outer_fun
def new(x,y):
    return x+y
    # input
p=int(input("enter a no."))
q=int(input("enter a no."))
new(p,q)


