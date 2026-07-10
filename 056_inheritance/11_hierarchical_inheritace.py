#11_hierarchical_inheritace

class A:

   def show1(self):

       print("A")

class B(A):

   def show2(self):

       print("B")

class C(A):

   def show3(self):
 
      print("C")

obj = C()

obj.show1()

'''
#obj.show2()   AttributeError: 'C' object has no attribute 'show2'. Did you mean: 'show1'?
'''
obj.show3()

'''
A
C
'''

obj1 = B()
obj1.show1()
obj1.show2()

#obj1.show3()
'''
AttributeError: 'B' object has no attribute 'show3'. Did you mean: 'show1'?
'''

'''
A
B
'''



 