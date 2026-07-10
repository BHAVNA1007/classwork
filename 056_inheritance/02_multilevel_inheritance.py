#02_multilevel_inheritance

class GrandParent:

    def fun1(self):
 
        print("from Grandparent")

class Parent(GrandParent):

    def fun2(self):
  
        print("from parent")

class Child(Parent):

    def fun3(self):
   
        print("from child")

obj = Child()

obj.fun1() 
obj.fun2() 
obj.fun3() 

'''
from Grandparent
from parent
from child

'''