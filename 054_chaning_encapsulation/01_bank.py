#01_bank

class Bank:

    def __init__(self, balance):
         self.__balance = balance

    def get_balance(self):
         return self.__balance

    def deposite(self, amount):
         
        if amount > 0: 
            self.__balance +=  amount
            print("amount: ", amount)
        else:
            print("Invalid deposite")
            

    def withdraw(self, amount):

        if amount <= self.__balance:

           self.__balance -= amount
           print("amount after withdraw ", amount)

        else:
           print("Insufficient")  

    def display(self):
        print("Current balanc:", self.__balance)


s1 = Bank(100)

print(s1.get_balance())
s1.deposite(500)
s1.withdraw(300)

s1.display()

                     

     