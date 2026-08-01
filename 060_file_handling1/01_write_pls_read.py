#01_write_pls_read


'''
try:
   with open("file1.txt", "w") as f:
      f.write("file handling in python")
      print("written")

except FileNotFoundError as e:
    print(e)

print("rest of the code")
'''

'''
written
rest of the code
'''




try:
   with open("file2.txt", "w+") as f:
      f.write("helloooooo i am here....")
      print("written")
      f.seek(0)
      data = f.read()
      print(data)
except FileNotFoundError as e:
    print(e)

print("rest of the code")  






'''
written
helloooooo i am here....
rest of the code
'''

      
    