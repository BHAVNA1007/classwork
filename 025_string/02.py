s = input("Enter the string: ")
s1 = ''
s2 = ''
result = ''

for ch in s:
   if (ch<='z' and ch>='a') or (ch<='9' and ch>='0'):
     if ch.isalpha():
        s1 = s1+ch
     else:
        s2 = s2+ch

for ch in sorted(s1):
    result = result + ch

for ch in sorted(s2):
    result = result + ch
print(result)