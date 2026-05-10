'''
02_in_operator_with_if
'''

s = input("Enter the string = ")

for ch in s:
    if ch in 'aeiouAEIOU':
        continue
    print(ch, end=' ')
   