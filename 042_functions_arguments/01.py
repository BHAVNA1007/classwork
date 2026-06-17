#arguments
'''
def sum(a,b):
    c = a+b 
    return c 
    
def main():    
    x = sum(10,20)
    c = sum(11,22)
    print(sum(66,77))
    print(c)
    print(x)
main()    
'''
'''
143
33
30
'''

'''
def sum(a,b):
    c = a+b 
def main():
   print(sum(10,20))    
   x = sum(11,99)
   print(x)
main()   
'''
'''
None
None
'''



'''
# here is some correction needed actually it thows error
def sum(a,b):
    c = a+b 
    return c
def main():
    print(sum(10,20))
    print(c)   # c not defined
main()    
'''


emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]
dic={}
for i in range(len(emails)):
   # j=emails[i].split("]")[0][1:].split("@")[1]
    j=emails[i].split("]")[0].split("@")[1]
    print(j)
    #dic[j]=dic.get(j,0)+1       