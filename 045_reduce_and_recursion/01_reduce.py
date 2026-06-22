#01_reduce

from  functools import reduce

def add(x,y):
   return x+y

numbers = [1,2,3,4,5,6]

result = reduce(add, numbers)
print(result)#21


result = reduce(add, numbers, 100) #including initilizer
print(result)#121

#using lambda function

result = reduce(lambda x,y:x+y, numbers)
print(result)#21

result = reduce(lambda x,y:x+y, numbers, 10)
print(result)#31

result = reduce(lambda x,y:x*y, numbers)
print(result)#720


num = [11,2,333,4,5,6]
result = reduce(lambda x,y: x if x>y else y, num)
print(result)#333




