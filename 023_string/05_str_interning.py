#05_str_interning

a = "welcome"
b = "welcome"

a[1]="x"

print(id(a))
print(id(b))

'''
    a[1]="x"
    ~^^^
TypeError: 'str' object does not support item assignment
'''