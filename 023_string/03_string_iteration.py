#string_iteration


s1 = "welcome"

for ch in s1:
   print(ch)

s2 = "welcome"

count = 0

for ch in s2:
   count += 1
print(count)  


s3 = input("Enter a string: ")
i = 0

while i < len(s3):
   print(i," ",s3[i])
   i += 1


str = "welcome"
for i in range(len(str)):
   print(i, " ",str[i])


for i, ch in enumerate(str):
   print(i," ",ch)
    









