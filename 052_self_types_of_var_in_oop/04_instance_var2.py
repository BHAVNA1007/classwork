#04_instance_var

class Student:
  
    def set(self, name, age):
        self.name = name
        self.age = age

s1 = Student()
s2 = Student()

s1.set("deepika", 30)
s2.set("rash", 33)

print(s1.name)
print(s2.name)

s1.name = "dipu"

print(s1.name)
print(s2.name)



#another way

class Student1:

   pass

s1 = Student1()
s1.name = "Bhavna"

print(s1.name)
