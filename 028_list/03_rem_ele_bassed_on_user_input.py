'''
#03_rem_ele_bassed_on_user_input

a = ['deep','rash','www','rrr']
name = input('enter name: ')
if name in a:
    a.remove(name)
else:
    print('name not found')
print(a)
'''

'''
#here changes reflects only list a not in b both have diff #ref
a = ['deep','rash','www','rrr']
b = ['deep','rash','www','rrr']
name = input('enter name: ')
if name in a:
    a.remove(name)
else:
    print('name not found')
print(b)
print(a)
'''


#here changes reflects in both list a , b both have same #reffrence
a = ['deep','rash','www','rrr']
b = a
name = input('enter name: ')
if name in a:
    a.remove(name)
else:
    print('name not found')
	print(b)
print(a)


