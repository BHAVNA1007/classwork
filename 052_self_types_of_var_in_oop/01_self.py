#01_self

class  Hello:
   def __init__(self):
       print("address of self: ", id(self))

obj = Hello()

print("address of obj: ", id(obj))


