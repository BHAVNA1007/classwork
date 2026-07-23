#01_isinstance

class A:
   pass

class B(A):
   pass

obj1 = B()
print(isinstance(obj1,B)) #True
print(isinstance(obj1,A))  #True

obj2 = A()
print(isinstance(obj2, B))  #False