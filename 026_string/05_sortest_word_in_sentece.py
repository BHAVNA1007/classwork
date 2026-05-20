'''
05_sortest_word_in_sentece
'''
s = input('Enter the string: ')
words = s.split()

short = words[0]

i = 1
while i < len(words):
   if len(words[i])<len(short):
       short = words[i]
   i = i+1 

print('Shortest word he', short)