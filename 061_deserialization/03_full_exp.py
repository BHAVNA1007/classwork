#03_full_exp



import pickle

class Employee:

   def __init__(self, id, name, salary):
       self.id = id
       self.name = name
       self.salary = salary
   
   def display(self):
       print("id : ", self.id)
       print("name: ", self.name) 
       print("salary: ", self.salary)

e1 = Employee(101, "bhavna", 200000)

file = open("empdata.dat", "wb")
pickle.dump(e1, file)

file.close()
print("serialization done")

file = open("empdata.dat", "rb")
newobj = pickle.load(file)

file.close()

print(newobj)
newobj.display()
print("deserialization done")



'''

serialization done
<__main__.Employee object at 0x0000023EAC887440>
id :  101
name:  bhavna
salary:  200000
deserialization done
'''
   