#10 multiple inheritace

class A:

   def show(self):
  
      print("A")

class B:
 
   def show(self):

       print("B")

class C(B, A):

   def show(self):

      A.show(self)
      B.show(self)
    
      print("C")

obj = C()

obj.show() 


'''
A
B
C
'''