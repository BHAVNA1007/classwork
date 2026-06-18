#02_add_two_list
#using normal function

l1 =[10,20,30]
l2 =[100,200,300]

def add(a,b):
    return a+b
r = map(add, l1,l2)
print(list(r))

'''
using lambda

l1 =[10,20,30]
l2 =[100,200,300]

r = map(lambda a,b:a+b, l1,l2)
print(list(r))    #[110, 220, 330]
'''
