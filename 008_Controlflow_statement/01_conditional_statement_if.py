'''
conditional_statement_if
Syntax -
if condition:
    statement1
    statement2
statement3

here this third statement not throw error

In the above syntax statement1 and statement2 are inside the if block and statement3 is outside the if block.

'''

'''
if True:
    print("welcome")
'''

'''
IndentationError: expected an indented block after 'if' statement on line 18
if True:
print("welcome")
'''

'''
if True:
    print("wlcome")
print("done")
'''

'''
a=10
b=20
if a>b:
    print("a is greater")
    print("a is greater then b")
if b>a:
    print("b is greater")
    print("b is greater than a")
print("Done")
'''

'''
a = int(input("Enter a number = "))
if a%2 == 0:
    print("a is even")
if a%2 != 0:
    print("a is odd")
print("Done")
'''


name = input("enter the name = ")
if name:
    print("name is enterd is ", name)
print("done")
   







