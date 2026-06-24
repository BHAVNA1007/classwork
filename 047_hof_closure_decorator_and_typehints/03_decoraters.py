#03_decoraters
'''
#tradisnal way to create decorater

def mydesign(func):

    def wrapper():

        print("befor calling the code")
        func() #call original funvction
        print("after calling the code")

    return wrapper

def hello():
    print("hello gyus how is the life is going on") 

d = mydesign(hello)

d()
'''

#modern way to create decorator

def mydesign(func):

    def wrapper():

        print("befor calling the code")
        func() #call original funvction
        print("after calling the code")

    return wrapper

@mydesign
def hello():
    print("hello gyus how is the life is going on")

hello() 



#anoter example of decorater

loggedin = True

def loginrequired(func):

    def wrapper():

        if loggedin:
           print("processing")
           func()
        else: 
           print("plz login...")

    return wrapper

@loginrequired  
def profile():
    print("welcom to our page")

profile()


@loginrequired
def transaction():
    print("Transaction done..")

transaction()



