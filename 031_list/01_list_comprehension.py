#01_list_comprehension
#normal way
a = [1,2,3,4,5]
b = []

for i in a:

   b.append(i*2)

print(b)


#now come on list comprehension:

a = [1,2,3,4,5]
b = [i*2 for i in a]
print(b)
