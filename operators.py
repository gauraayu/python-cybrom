# logical operators ()
#  return boolea value

x=10
y=20
z=30
print(not(x<y)and(y<z))
print((x>y)or(y<z))

# membership operators()
# keywords used are= in /not in 
# return boolean values
str1="aayu"
print('n'in str1)
print('n' not in str1)


# idenitty operator()
# keywords = is/is not
x=10
y=10
print(x is y)
# o/p=true
print(id(x))
print(id(y))
# memory addres same
# print (x is not y)

x=[10]
y=[10]
print (x is y)
# o/p=false 
print(id(x))
print(id(y))
