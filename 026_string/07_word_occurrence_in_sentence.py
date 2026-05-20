'''
07_word_occurrence_in_sentence
'''
s = input('Enter the string: ')
word = input('Enter the word: ')

count = 0
i = 0
while i < len(s) - len(word):
   j = 0
   match = 1
   while j < len(word):
      if s[i+j] != word[j]:
         match = 0
         break
      j = j + 1
   if match == 1:
      count = count + 1
   i = i + 1

print('Number of occurrencess: ', count) 


