def first():
    return 'hello'
x=first()
print(x) #o/p hello  in case of return

# USING YIELD 
# yield is only used in generator
def first():
    yield 1
    yield 2
    yield 3
x=first()  #genrator has become object as we have used yield
# print(list(x))
print(next(x))
print("hi")
print("hello")
print("welcome")
print(next(x))
print("hello")
print("welcome")
print(next(x))
# THIS WILL GIVE ERROR
# print("hello")
# print("welcome")
# print(next(x))



