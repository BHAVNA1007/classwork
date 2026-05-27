#004_comparing_list_object
'''
a=["deepika","rashmika","katappa"]
b=["deepika","rashmika","katappa"]
c=["DEEPIKA","RASHMIKA","KATAPPA"]

print(a==b)
print(a==c)
print(a!=c)

print(a is b)
print(id(a))
print(id(b))

print(id(a[0]))
print(id(b[0]))
print(a[0] is b[0])
'''

a = [50,40,30]
b = [20,30,100,50]
print(a>b)

a = [50,40,30]
b = [200,30,100,50]
print(a>b)

a = [200,40,30]
b = [200,30,100,50]
print(a>=b)

a=['deepika','rashmika']
b=['DEEPIKA','rashmika']
print(a>b)

a=['Deepika','rashmika']
b=['dEEPIKA','rashmika']
print(a>b)



