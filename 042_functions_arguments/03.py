#03

def calculate(a,b):
    return a+b, a-b 
    
def main():
    print("welcome")
    result = calculate(10,5)
    #sum,diff = calculate(10,5)
    print(result)
    print("sum is: ", result[0])
    print("diff is ", result[1])
main()    
'''
welcome
(15, 5)
sum is:  15
diff is  5
'''

def calculate(a,b):
    return a+b, a-b 
    
def main():
    print("welcome")
 
    sum,diff = calculate(10,5)
    print("sum is: ", sum)
    print("diff is ", diff)
main()    