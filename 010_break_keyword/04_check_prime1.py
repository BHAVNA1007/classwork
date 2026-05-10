'''
04_check_prime1

'''
n = int(input("Enter a number = "))

if n <= 1:
    print("not prime number ")
else:
    x = 0
    i = 2
 
    while i < n:
        if n % i == 0:
            x = 1
            break
        i += 1
    if x == 0:
        print("prime number")
    else:
        print("Not prime")