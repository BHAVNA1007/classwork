'''
02_rev_sen_each_word
'''

s = input('Enter the string: ')
words = s.split()
i = len(words)-1

while i>=0:
   word = words[i]
   rev = ''
   j = len(word)-1
   while j >= 0:
      rev = rev + word[j]
      j = j -1
   print(rev, end=' ')
   i = i - 1 