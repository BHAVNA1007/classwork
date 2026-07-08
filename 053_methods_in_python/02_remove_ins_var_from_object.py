#02_remove_ins_var_from_object

class Test:

    def __init__(self):

        self.a = 10
        self.b = 20
        self.c = 30

t1 = Test()
t2 = Test()

del t1.c
del t2.b

print(t1.__dict__)
print(t2.__dict__)

'''
{'a': 10, 'b': 20}
{'a': 10, 'c': 30}

'''


