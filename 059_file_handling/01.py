# open()
'''
f = open("00.txt")
print(f)
'''
'''
FileNotFoundError: [Errno 2] No such file or directory: '00.txt'

'''


'''
f = open("f1.txt","r")
print(f.name)

#f1.txt
'''


'''
f = open("f1.txt","r")
print(f.mode)

#r
'''



'''
f = open("f1.txt", "r")
print("is closed: ", f.closed)

#is closed:  False

f.close()
print("is closed: ", f.closed)

#is closed:  True
'''




'''
f = open("f1.txt", "r")

data = f.read()
print(data)

f.close()

#hi I am her
'''



'''
f = open("f1.txt", "w")
f.write("i am here for learn python")
print("plz check me")
f.close()
'''

















