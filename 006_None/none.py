#None is to difine a null value. it is not the same as an #empty strig, a false value or 0

print(type(None))

#NameError: name 'x' is not defined
'''
x
print(type(x))
'''

'''
#NameError: name 'none' is not defined. Did you mean: 'None'?
x=none
print(type(x))
'''

'''
x=None
print(type(x))
'''

print(None==0)
print(None==False)
print(None=="")
print(None==[])

'''
NameError: name 'null' is not defined
print(None==null)
'''
print(None==None)




'''
usage of none:

1.defalult function return: if a function does not explitly return a value python automaticaly return None

placeholder for variables: it help to assign value to a variable when you want to initialize it but do not have a value
'''