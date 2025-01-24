str1='PYTHON'
print(str1.index('T'))
print(str1.index('P'))
print(str1.index('O'))
# print(str1.index('t'))  will show error
# print(str1.index('T',3)) #this will start searching after 3rd index and thid will show error
# print(str1.index('obj',start,stop))
print(str1.index('T',0,4))   #0 is start point #4 is the end point for searching