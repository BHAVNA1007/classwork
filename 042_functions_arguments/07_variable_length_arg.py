#07_variable_length_arg

'''
def display(*args):
    print(args)
display(1,2,3,4,5,6)
    
#(1, 2, 3, 4, 5, 6) 
'''   

'''
def display(*args):
    print(args)
display(1,2,"bhavna",5,"hello")

#(1, 2, 'bhavna', 5, 'hello')
'''

def sum(*a):
    total = 0
    for n in a:
        total = total + n 
    print(total) 
sum(10,20,30) #60
sum(10,20,30,60,70,80) #270
sum(10,20) #30
sum(10)  #10
sum()    #0