#03_nonlocal

def outer():

    x = 10
    
    def inner():
        nonlocal x
        x = 100
        print("inner value of",x)
    inner()
    print("inside outer", x)

outer()

'''
inner value of 100
inside outer 100
''' 