#05_keyword_only_parameter

def show(name, *, age, address):
   print(name)
   print(age)
   print(address)

show("deepika", age=30, address="chennai")
'''
deepika
30
chennai
'''
'''
show("deepika", 30, "chennai")
TypeError: show() takes 1 positional argument but 3 were given
'''