#07_all_parameters


def show(id, name, /, salary, *, age, address):
   print(id)
   print(name)
   print(salary)
   print(age)
   print(address)

show(111,"deepika",3000,age=30,address="chennai")
'''
111
deepika
3000
30
chennai
'''
'''
show(id=111,"deepika",3000,age=30,address="chennai")
SyntaxError: positional argument follows keyword argument
'''