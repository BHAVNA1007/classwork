#17-06-26

def hello(name, *marks):
   print("name is: ", name)    #name is:  deepika
   print("marks is: ",marks)    #marks is:  (10, 20, 30)
   print("marks is: ", *marks)  #marks is:  10 20 30
hello("deepika",10,20,30) 


'''
def hello(*marks, name):
   print("name is: ", name)    
   print("marks is: ",marks)    
   print("marks is: ", *marks)  
hello("deepika",10,20,30)
hello("deepika",10,20,30)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: hello() missing 1 required keyword-only argument: 'name'
'''
 

