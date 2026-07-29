#03_file_mode   
#write mode

'''
try:

    with open("f1.txt", "w") as f:
       f.write("helooo")
       print("check me changes")
       print(f.closed)

except FileNotFoundError as e:
    print(e)
  
'''  





'''
try:

    with open("f1.txt", "w") as f:
       data = f.read()
       print(data)
       print(f.closed)

except FileNotFoundError as e:
    print(e)

#io.UnsupportedOperation: not readable

'''



# append mode
'''
try:

    with open("f1.txt", "a") as f:
       f.write("i want to learn everything")
       print("check me changes")
       print(f.closed)

except FileNotFoundError as e:
    print(e)

'''



'''
try:

    with open("f1.txt", "a") as f:
       data = f.read()
       print(data)
       print(f.closed)

except FileNotFoundError as e:
    print(e)
#io.UnsupportedOperation: not readable
'''



'''
# x mode
try:
   with open("f1.txt", "x") as f:
       f.write("i want to learn everything")
       print("check me changes")
       print(f.closed)

except FileNotFoundError as e:
    print(e)
#FileExistsError: [Errno 17] File exists: 'f1.txt'
'''

'''
try:
   with open("f2.txt", "x") as f:
       f.write("i want to learn everything")
       print("check me changes")
       print(f.closed)

except FileNotFoundError as e:
    print(e)
'''

'''
try:
    with open("f3.txt", "x") as f:
       data = f.read()
       print(data)
       print(f.closed)

except FileNotFoundError as e:
    print(e)
#io.UnsupportedOperation: not readable
'''



# r+


try:
    with open("f3.txt", "r+") as f:
       data = f.read()
       print(data)

       f.write("now, I am at right track")
       print(f.closed)

except FileNotFoundError as e:
    print(e)


