#06_class_var2

class Test:

    x = 10

t1 = Test()
t2 = Test()

t1.x = 90

print(t1.x)
print(t2.x)

print(Test.x)

print(t1.__dict__)

Test.x = 100

print(t1.x)

print(t2.x)

Test.y = 900

print(t1.y)



class Test1:

   def __init__(self):

       self.a = 10
       self.b = 20

   def m1(self):
 
       self.c = 30
       self.d = 40

t1 = Test1()
t1.m1()
t1.e = 900
print(t1.__dict__)

#{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 900}



class Test2():

   a = 10
  
   def __init__(self):

       self.b = 20
       Test2.c = 30

   def m1(self):
       Test2.d = 100

t1 = Test2()
t1.m1()

t2 = Test2()
print(t1.__dict__)

print(t2.a)

print(t2.c)

print(t2.d)

print(Test2.__dict__)

'''
{'b': 20}
10
30
100
{'__module__': '__main__', 'a': 10, '__init__': <function Test2.__init__ at 0x000002716FF59260>, 'm1': <function Test2.m1 at 0x000002716FF59300>, '__dict__': <attribute '__dict__' of 'Test2' objects>, '__weakref__': <attribute '__weakref__' of 'Test2' objects>, '__doc__': None, 'c': 30, 'd': 100}
'''








