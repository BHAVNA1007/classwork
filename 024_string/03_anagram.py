'''
03_anagram
'''
s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')

if len(s1) == len(s2):
    if sorted(s1) == sorted(s2):
        print('Anagram')
    else:
        print('not annagram')
else:
    print('not anagram')   



s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')

if len(s1) != len(s2):
    print("not anagram")

else:
    f = 1
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            f = 0
            break 
    if f==1:
         print(" anagram") 
    else:
         print('not anagram')    
    