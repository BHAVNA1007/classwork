'''
06_rev_each_word
'''

s = input('Enter the string: ')
words = s.split()
i = 0

while i <len(words):
    word = words[i]
    rev = ''
    j = len(word)-1
    while j >= 0:
       rev = rev + word[j]
       j = j-1
    print(rev,end=' ')
    i += 1    
  

s = input('Enter the string: ')
words = s.split()
for word in words:
    print(word[::-1],end=' ')


s = input('Enter the string: ')
rev = s[::-1]
rev2 = rev.split()
print(' '.join(rev2[::-1]))

