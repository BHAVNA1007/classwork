s = input('Enter the string : ')
res = ''
prev =''

for ch in s:
   if ch.isalpha():
       res = res+ch
       prev = ch
   else:
       newch = chr(ord(prev)+int(ch))
       res = res + newch

print(res)