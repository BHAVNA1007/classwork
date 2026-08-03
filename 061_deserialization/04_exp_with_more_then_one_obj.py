#04_exp_with_more_then_one_obj


import pickle

class Employee:
  
   def __init__(self, id, name, salary):
       self.id = id
       self.name = name
       self.salary = salary

   def display(self):
       print("ID: ", self.id)
       print("Name: ", self.name)
       print("Salary: ", self.salary)

employees = [
    Employee(101, "bhavna", 800000),
    Employee(102, "Umesh", 900000),
    Employee(103, "titali", 7000000)
]

file = open("empdata.dat", "wb")
pickle.dump(employees, file)

file.close()
print("serealization done")


file = open("empdata.dat", "rb")

objlist = pickle.load(file)

file.close()

for e in objlist:
   print(e.id, "and", e.name)

print("done")


'''
serealization done
101 and bhavna
102 and Umesh
103 and titali
done
''

  