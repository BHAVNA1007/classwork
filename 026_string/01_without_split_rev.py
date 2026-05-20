'''
01_without_split_rev
'''

s = input('Enter the stirng: ')
word = ''
i = 0 
while i < len(s):
   if s[i] != ' ':
      word = s[i] + word
   else:
      print(word, end= ' ')
      word  = ' '
   i = i + 1
print(word, end=' ') 