#01_merge_two_list_without_duplicate

n = int(input('Enter the size: '))
l1 = []
print('plz enter the ele...: ')

for i in range(n):
    l1.append(int(input()))
print(l1)

l2 = []
print('plz enter the ele...: ')

for i in range(n):
    l2.append(int(input()))
print(l2)

merge = l1 + l2

result = []
for i in merge:
   if i not in result:
       result.append(i)

print(result)


