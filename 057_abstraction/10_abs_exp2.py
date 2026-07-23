#10_abs_exp2


from abc import ABC, abstractmethod

class Payment(ABC):
   @abstractmethod
   def pay(self):
       pass

class UPI(Payment):
    def __init__(self, amount):
       self.amount = amount

    def pay(self):
       print("Amount from UPI...", self.amount)

class Netbanking(Payment):
    def pay(self):
        print("Amount from Netbanking...")

class Creditcart(Payment):
    def pay(self):
        print("Amount From Creditcart...")

u = UPI(100)
u.pay()

n = Netbanking()
n.pay()

c = Creditcart()
c.pay()
    