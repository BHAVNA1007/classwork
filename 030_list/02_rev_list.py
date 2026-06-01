#02_rev_list
'''
n = int(input('Enter the size: '))
l = []
print('plz enter the ele...: ')

for i in range(n):
    l.append(int(input()))
print(l)

l.reverse()
print(l)

rev = l[::-1]
print(rev)

'''
n = int(input('Enter the size: '))
l = []
print('plz enter the ele...: ')

for i in range(n):
    l.append(int(input()))
print(l)

rev = []
for i in l:
   rev =[i] + rev
print("REVERSED: ",rev)




