#02_issubclass

class A:
   pass

class B(A):
   pass

obj1 = B()
print(issubclass(B,A)) #True

print(issubclass(A, B)) #False