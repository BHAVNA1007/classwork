#07_cyclic_rotated_by_one

n = int(input('Enter the size: '))
print("plz enter ele...")

l = []
for i in range(n):
    l.append(int(input()))
print(l)

last = l[n-1]

i = n-1

while i > 0:
   l[i] = l[i-1]
   i = i - 1

l[0] = last
print(l)
