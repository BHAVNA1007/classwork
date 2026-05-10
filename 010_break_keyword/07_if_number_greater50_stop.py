'''
07_if_number_greater50_stop
'''
n = int(input("Enter a number = "))

for i in range(1, n):
    if n*i >= 50:
        break
    print(i*n)