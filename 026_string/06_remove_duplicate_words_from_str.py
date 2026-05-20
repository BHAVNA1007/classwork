'''
06_remove_duplicate_words_from_str
'''
s = input("Enter String: ") 
words = s.split() 
i = 0
unique = []
while i< len(words):       
   count = 0
   j = 0
   while j < len( unique):
      if words[i].lower() == unique[j].lower():
         count = count + 1
      j = j + 1

   if count == 0:
      unique.append(words[i])
   i  = i + 1

i = len(unique) - 1
while i >= 0:
    print(unique[i].title(),end=' ')
    i = i - 1     
      