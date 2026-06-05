from collections import namedtuple

Account = namedtuple("Account",['accno','holdername','balance'])

ano = int(input("enter account number: "))
name = input("enter holder's name: ")
b = float(input("enter balance: "))

acc = Account(ano,name,b)
print(acc.accno)
print(acc.holdername)
print(acc.balance)



