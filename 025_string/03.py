s = input('Enter the string: ')
res = ''
prev =''
for x in s:
  if x.isalpha():
     res = res + x
     prev = x
  else:
     res = res + prev*(int(x)-1)

print(res)

