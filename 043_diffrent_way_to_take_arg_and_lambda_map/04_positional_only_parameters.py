#04_positional_only_parameters

def display(name, age, /):
    print(name,age)   #deepika 30
display("deepika", 30)


#normal 
def add(a,b,c):
   print(a+b+c)
add(10,20,30)  #60
add(a=100, b=200, c=300)  #600

'''
#with positional only
def add(a,b,c,/):
   print(a+b+c)
add(10,20,30) #60
add(a=100, b=200, c=300)

TypeError: add() got some positional-only arguments passed as keyword arguments: 'a, b, c'
'''


 
 