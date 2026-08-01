#03_binary_mode

'''
#read binary ----->>>> "rb"

f1 = open("picture.jpg", "rb")
data = f1.read()



#write binary ---->>>>  "wb"


f2 = open("pic.jpg","wb")
f2.write(data)
print("done")

'''




'''
#append binary ---->>>>  "ab"


with open("file3.txt", "ab") as file:

   file.write(b"i am in append mode")


   #data = file.read()
   #print(data) 

# reading is not allowed --- io.UnsupportedOperation: read
'''





'''
#If we want BOTH append and read use --->  "ab+"

with open("file3.txt", "ab+") as file:

    file.write(b"now i am in ab+ mode")
    file.seek(0)
    data = file.read()
    print(data) 

'''
    
  
'''
ab+ 
│││
││└── + = reading + writing
│└─── b = binary
└──── a = append


file.seek(0)

before read(), otherwise the file position is at the end and you may get empty data.

'''  
 




'''
# read + write  ----->>>> "rb+"
#here first we need to create file    
# if file not exists then it throw FileNotFoundError   

with open("file4.txt", "rb+") as file:

   file.write(b"now again one feature r+w binary file")
   file.seek(0)
   data = file.read()
   print(data)
'''





# read + write  ---->>>  "wb+"

with open("file5.txt", "wb+") as file:
   
   file.write(b"hello i am in wb+ mode")
   file.seek(0) 
   data = file.read()
  
   print(data)




'''
rb+ → Read + Write without deleting existing content.

wb+ → Read + Write after deleting existing content (or creating a new file).
'''
