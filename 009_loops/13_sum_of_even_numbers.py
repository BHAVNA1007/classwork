#13_sum_of_even_numbers

'''
num = int(input("Enter a number = "))
sum = 0

for i in range(1,num+1):
    
    if i % 2 == 0:
       sum += i
print(sum)
'''

num = int(input("Enter a number = ") )
sum = 0
for i in range(2, num+1, 2):
    sum += i
print(sum)


