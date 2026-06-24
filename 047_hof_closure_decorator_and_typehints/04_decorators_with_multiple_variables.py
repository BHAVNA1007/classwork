#04_decorators_with_multiple_variables

def mydecorator(func):

    def wrapper(*args,**kwargs):
    
        print("calculation starting...")
        result = func(*args, **kwargs)
        print("calcutation done")
        return result
    return wrapper

@mydecorator
def add(a,b):
    print("sum is", a+b)

@mydecorator
def product(a,b,c):
    print("product is: ",a*b*c)

add(20,30)

product(10,20,30)

