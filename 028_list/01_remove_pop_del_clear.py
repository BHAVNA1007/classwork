#01_remove_pop_del_clear

'''
#remove()

a = [10,20,30,40,10]
print(a)
a.remove(10)
print(a)
#if we want to save removed element it will show None
x = a.remove(10)
print(x)

'''

'''
# if value not in list it throw ValueError : x not in list
a.remove(90)
print(a)
'''

'''
a = [10,20,30,40,10]
print(a)
a.pop()
print(a)


a.pop(0)
print(a)
'''

'''
#here indexError ocuure because 7 index is not exits
#IndexError: pop index out of range
a = [10,20,30,40,10]
a.pop(7)
print(a)
'''

'''
# when pop value and retun it ans is popped value but
# in  case of remove return value is None  
a = [10,20,30,40,10]
x = a.pop(1)
print(a)
print(x)

y = a.remove(30)
print(y)
'''

'''
#clear(): empty the whole list
a = [10,20,30,40,10]
print(a)
print(len(a))

a.clear()
print(a)
print(len(a))
'''

#del keyword
a = [10,20,30,40]
print(a)
del a[1]
print(a)


a=[10,20,30,40,50,10]
print(a)
del a[1:4]
print(a)

#NameError: name 'a' is not defined
del a
print(a)


