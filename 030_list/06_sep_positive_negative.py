#06_sep_positive_negative

n = int(input('Enter the size: '))
print("plz enter ele...")

l = []
for i in range(n):
    l.append(int(input()))
print(l)

positive = []
negative = []

for i in l:
   if i > 0:
       positive.append(i)
   else:
       negative.append(i)

result = positive + negative
print(result)

