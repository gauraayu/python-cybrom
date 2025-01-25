s1='python'
print(s1[:])
# 1. step ka directn nhi dia toh by default +ve 
# 2.  +ve directn
# 3.  o/p=python
s2='python'
print(s2[::]) 
# 1. step directn=+ve
# 2.  +ve directn
#  3.o/p= python
 
s3='python'  
print(s3[::-1])  #kisi b collectn ko reverse krne ka y slice hota h 
# 1. step directn=-ve
# 2. -ve directn
# 3. o/p=nohtyp

# empty o/p
s4='i love python'
print(s4[-1:-2:2])  # yhn 2 lia    mtlb 2 units chorkr print krna h 
# 
s5='i love python'
print(s5[:-2:-2])