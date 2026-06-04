#06_tuple_example


id = int(input("enter id:"))
name = input("enter name:")
salary = int(input("enter salary:"))

employee = (id, name, salary)
print("employee details")
print("id:",employee[0])
print("name:",employee[1])
print("salary:",employee[2])


'''
enter id:2
enter name:bhavna
enter salary:1200
employee details
id: 2
name: bhavna
salary: 1200
'''