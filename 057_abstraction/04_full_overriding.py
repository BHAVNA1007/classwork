#04_full_overriding


class Employee:
    def salary(self, basic, bonus):
        print("total salary: ", basic + bonus)

class Manager(Employee):
    def salary(self, basic, bonus):
        print("Manager salary: ", basic + bonus + 500)

obj1 = Manager()   
obj1.salary(2000, 100) #Manager salary:  2600

