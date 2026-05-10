'''
02_exception_in_for_else
'''

for i in range(1, 10):
    print(i)
    if i == 20: #exception lies here
         break
else:
    print("No break")