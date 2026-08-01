#02_append_pls_read


try: 
  with open("file2.txt","a+") as f:
     f.write("are... yes/no")
     print("append and read check")
     f.seek(0)
     data = f.read()
     print(data)

except  FileNotFoundError:
   print("file not found") 

print('rest of the code')