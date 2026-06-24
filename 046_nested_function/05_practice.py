##05_practice

def total(price, taxrate):
    def calculatetax():

        return price*taxrate

    return price + calculatetax()   
print(total(1000, 0.18))  #1180.0



def bill(amount):
   def discount():
      if amount > 10000:
         return amount * 0.10
      return 0
   d = discount()
   finalamount = amount - d 
   return finalamount
print(bill(15000))

'''
1180.0
13500.0
'''
  
