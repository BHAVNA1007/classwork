#03_kwargs

def display(**kwargs):
   print(kwargs)
display(name="deepika",age=30,address="mumbai")
#{'name': 'deepika', 'age': 30, 'address': 'mumbai'}

def display(**kwargs):
  for key, v in kwargs.items():
      print(key,":", v) 
display(name="deepika",age=30,address="mumbai")

'''
name : deepika
age : 30
address : mumbai

'''



