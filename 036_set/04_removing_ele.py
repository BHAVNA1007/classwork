#04_removing_ele

'''
s = {10,20,30,40,50}
s.remove(20)
print(s)  # {50, 40, 10, 30}
'''

'''
s.remove(22)
print(s) #KeyError: 22
'''

#s.discard(22)


#pop
'''
s = {10, 20, 30, 40}
print(s)   #{40, 10, 20, 30}
s.pop
print(s)
'''

'''
s = set()
s.pop()
print(s)
'''

'''
s = {10, 20, 30, 40}
print(s)   #{40, 10, 20, 30}
del s
print(s)  #NameError: name 's' is not defined
'''
#clear():  it remove all the elements

s = {1,2,3,4}
print(s)            #{1, 2, 3, 4}
s.clear()
print(s)     #set()

