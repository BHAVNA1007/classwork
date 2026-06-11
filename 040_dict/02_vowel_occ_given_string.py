#02_vowel_occ_given_string

word = input("Enter word: ")
vowel = {'a', 'e', 'i', 'o', 'u'}

d = {}

for x in word:
    if x in vowel:
        d[x] = d.get(x,0)+1
        
print(d)        
  
for k, v in d.items():
    print(k, "occured", v , "times")    
