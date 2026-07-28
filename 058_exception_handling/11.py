#11


def withdraw(amount):

    balance = 5000

    if amount > balance:
       raise Exception("insufficient balance")

    return balance - amount 

try:
    print(withdraw(6000))

except Exception as e:
    print("Error", e)

print("rest of code")



   