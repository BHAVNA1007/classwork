#12_hybrid_inheritance

class A:

   def show1(self):
 
      print("A")

class B(A):

   def show2(self):

      print("B")

class C(A):

   def show3(self):

      print("C")

class D(B, C):

   def show4(self):

      print("D")

obj1 = D()

obj1.show1()  
obj1.show2()
obj1.show3()
obj1.show4()

print(D.mro())