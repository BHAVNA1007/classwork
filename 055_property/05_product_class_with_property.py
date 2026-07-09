#05_product_class_with_property

'''
wap for product class where id is read only , product title and product price

'''
class Product:

   def __init__(self, p_id, p_title, p_price):
       self.__p_id = p_id
       self.__p_title = p_title
       self.__p_price = p_price

   @property
   def p_id(self):
       return self.__p_id

   @property
   def p_title(self):
       return self.__p_title

   @p_title.setter
   def p_title(self, p_title):
       self.__p_title = p_title

   @property
   def p_price(self):
       return self.__p_price

   @p_price.setter
   def p_price(self, p_price):   
       self.__p_price = p_price  

p = Product(101, "iphone", 60000)
print(p.p_id)
print(p.p_title)
print(p.p_price)

'''
output:
101
iphone
60000
'''

'''
p.p_id = 102 AttributeError: property 'p_id' of 'Product' object has no setter

note: if we want to make any variable read only then we have no need to write setter 
'''
p.p_name = "Laptop"
p.p_price = 90000

print(p.p_id)
print(p.p_title)
print(p.p_price)

'''
output:
101
Laptop
90000
'''





   