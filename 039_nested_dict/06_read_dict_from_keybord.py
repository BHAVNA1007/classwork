#06_read_dict_from_keybord

#using eval

d = eval(input("Enter dict: "))
print(type(d))

print(d)
s = sum(d.values())
print(s)

'''
Enter dict: {"a": 22 ,"b": 11, "b": 55}
<class 'dict'>
{'a': 22, 'b': 55}
77
'''

# Mannually creation of dict

n = int(input("Enter number of items: "))

d = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
    
print(type(d))
print(d)

s = sum(d.values())
print("Sum of all values is: ", s)    
    
    