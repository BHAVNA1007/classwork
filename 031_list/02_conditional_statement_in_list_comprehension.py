#02_conditional_statement


a = [1,2,3,4,5,6,7,8]
b = [i for i in a if i%2==0]

print(b)


a = [1,2,3,4,5,6,7,8]
b = [i for i in a if i%2==0 and i>3] 
print(b)


a = [1,2,3,4,5,6,7,8]
b =["Even" if i%2==0 else "odd" for i in a]
print(b)


a = ["deepika","virat","RCB"]
b = [len(i) for i in a]
print(b)

a = ["deepika","virat","RCB"]
b = [i for i in a if len(i)>3]
print(b)


a = ["deepika","virat","RCB"]
b = [i.upper() for i in a]
print(b)


a = [11, 2, 3, 4, 5, 6]
b = [i*10 if i%2==0 else i for i in a]
print(b)

