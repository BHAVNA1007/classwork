#03_getter_and_setter

class Student:

    def setmarks(self, marks):
   
        self.marks = marks

    def getmarks(self):

        return self.marks

s1 = Student()

s1.setmarks(80)

print(s1.getmarks())   #80