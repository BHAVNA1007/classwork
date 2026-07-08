#05_static_method

class Calculator:

    @staticmethod

    def add(a, b):

        return a+b

c = Calculator()

print(c.add(10,20))

print(Calculator.add(10,20))

print(c.__dict__)

#print(Calculator.__dict__)


'''

30
30
{}
{'__module__': '__main__', 'add': <staticmethod(<function Calculator.add at 0x000001FF69D48FE0>)>, '__dict__': <attribute '__dict__' of 'Calculator' objects>, '__weakref__': <attribute '__weakref__' of 'Calculator' objects>, '__doc__': None}

'''


'''
we can call static method. either class name or by using object name
'''

class Demo:

   a = 10
   
   @staticmethod
   
   def display():
      #print(a)   #NameError: name 'a' is not defined
      print(Demo.a)   #10
c1 = Demo()
c1.display()  




class Student:
   college = "IIT"
   
   def set(self, name):
       self.name = name
   
   @staticmethod
   def display(x):
      print(Student.college) 
      #print(name) #name not defind
      #print(self.name) #self not defind
      print(x.name)  #Deepika

s1 = Student()
s1.set("Deepika")
s1.display(s1)
       
  
  

   






      
