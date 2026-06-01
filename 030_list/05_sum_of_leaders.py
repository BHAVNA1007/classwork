#05_sum_of_leaders

n = int(input('Enter the size: '))
print("plz enter ele...")

l = []
for i in range(n):
    l.append(int(input()))
print(l)


sum = 0
for i in range(n):
    isleader = True
    for j in range(i+1,n):
        if l[i] <= l[j]:
           isleader = False
           break
    if isleader:
        sum = sum + l[i]

print("sum of leader: ", sum)
