'''
05_rev_str_diff_ways
'''

s = input('Enter a string: ')
s1 = s[::-1]
print(s1)


s = input('Enter a string: ')
rev = ''
i = len(s)-1
while i>=0:
   rev += s[i]
   i = i -1
print(rev)

s = input('Enter a string: ')
s2 = s.split()
res =''
for i in range(len(s2)-1,-1,-1):
   res += s2[i]+' '
print(res)


s = input('Enter a string: ')
ls = s.split()
print(' '.join(ls[::-1]))
   
   