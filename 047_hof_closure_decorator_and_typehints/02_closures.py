###02_closures

'''
def hello(name):
 
   message = f"hello {name}"
   
   def display():

       print(message)

   return display

h = hello("deepika")

h()
'''
'''
def counter():

    count = 0

    def increment():

       nonlocal count
       count += 1
       return count

    return increment

c = counter()
print(c()) 
'''

def cardmaker(greeting,name):
    def card():
       return f"{greeting},{name}"

    return card

first = cardmaker("helooo","deepika")
second = cardmaker("hiiii","rashmika")

print(first())
print(second())

'''
print(first.__closure__)

if this print None it means it is not closure. if it return object it means it is a closure.
'''
