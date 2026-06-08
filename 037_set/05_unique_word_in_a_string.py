#05_unique_word_in_a_string

s = input("Enter a string: ")
s1 = s.split()

u = set(s1)

print(len(u))

another = list(u)
print(another)

s = input("Enter s string: ")

print(s)
print(set(s))

if len(s) == len(set(s)):
    print("no duplicate")
else:
    print("duplicate are there")    
 