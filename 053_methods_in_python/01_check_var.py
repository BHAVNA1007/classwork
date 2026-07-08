#01_check_var

class Test:

    a = 10

    def __init__(self):
        
        print(self.a)

t1 = Test()

print(t1.__dict__)

'''
10

{}

'''