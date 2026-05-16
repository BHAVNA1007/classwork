#immutability


'''
for satisfaction 
	
str = "welcome"
str[1] = 'r'
print(str)

'''
'''
str = 'welcome'
str = str +" "+ "home"

print(str)
'''

str ='welcome'
print(id(str))
str = str + "home"
print(id(str))