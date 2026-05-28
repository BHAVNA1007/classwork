#05_using_key

a=['deepika123','rashmika33','www1','rrr','deepika']

a.sort(key=len)
print(a)

a=[-10,-30,5,6,7,-8]
a.sort(key=abs)
print(a)

a=[-10,-30,5,6,7,-8]
a.sort(key=abs, reverse=True)
print(a)


a=['Deepika','deeepika','Rashmika']
a.sort(key=str.lower)
print(a)

