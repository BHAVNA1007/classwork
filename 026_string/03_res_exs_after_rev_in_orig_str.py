'''
03_res_exs_after_rev_in_orig_str
'''
s = input('Enter the string:  ')

words = s.split()

i = len(words)-1
final = ''
while i >= 0:
   word = words[i]
   rev = ' ' 
   j = len(word)-1
   while j >= 0:
       rev = rev + word[j]
       j = j -1
   final = final + rev + ' '
   i = i - 1

original = final.strip()
print('Updation in orinal srting: ',original)