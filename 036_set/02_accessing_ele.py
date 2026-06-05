#02_accessing_ele

s = {10,20,30,10,40}
#print(s[0])  #TypeError: 'set' object is not subscriptable
print(s)  #{40, 10, 20, 30}

for i in s:
    print(i)  

'''
40 
10
20
30
'''

print(20 in s)  #True

print(40 not in s) #False