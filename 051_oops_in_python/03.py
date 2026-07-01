#03

class Student:
    def set(self, id, name, address):
        print("Self is called...")
        self.id = id
        self.name = name
        self.address = address

    def display(self):
        print("Display is called...")
        print("ID is:", self.id)
        print("Name is: ", self.name)
        print("Address is: ", self.address)

s1 = Student()
s1.set(101, "bhavna", "Bhopal")
s1.display()


s2 = Student()
s2.set(102, "deepika", "hyd")
s2.display()

'''
Self is called...
Display is called...
ID is: 101
Name is:  bhavna
Address is:  Bhopal
Self is called...
Display is called...
ID is: 102
Name is:  deepika
Address is:  hyd
'''


     