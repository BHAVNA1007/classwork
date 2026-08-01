#04_functions_in_file_handling


#  tell()

f = open("file4.txt","r") 

print(f.tell())

print(f.read(3))

print(f.tell())

print("done") 


'''
0
now
3
done
''' 


# seek()


f = open("file4.txt", "r")

f.seek(5)

print(f.read())

print("done") 

'''
gain one feature r+w binary file
done
''' 


#readline()

f = open("file3.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline(2))

#data = f.readlines()
#print(data[0])

print(f.readlines())




