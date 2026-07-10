#08

class Father:

    def show(self):

        print("Father method is called...")

class Mother:

    def show(self):

        print("Mother's show method ")

class Child(Father, Mother):

   def show(self):

       super().show()

       print("Child's show method") 

c = Child()

c.show()

print(Child.mro())

'''

Child's show method
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]

'''



