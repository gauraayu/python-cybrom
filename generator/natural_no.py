def natural_no(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int(input("enter a no."))
p=natural_no(n)
#print(p)
# print(list(p))
print(next(p)) #o/p=1
print(next(p))  #o/p=2
for i in p:
    print(i) #o/p=3  hdjfi