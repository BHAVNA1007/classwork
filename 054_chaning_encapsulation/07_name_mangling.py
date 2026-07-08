#07_name_mangling


class Student:

      def __init__(self):

          self.__salary = 10000

s1 = Student()

print(s1._Student__salary)