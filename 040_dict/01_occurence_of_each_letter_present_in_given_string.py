'''
01_occurence_of_each_letter_present_in_given_string
'''

word = input("Enter word: ")
d = {}
for x in word:
    d[x] = d.get(x, 0)+1
print(d)  #{'h': 1, 'e': 1, 'l': 2, 'o': 1, 'w': 1}

    
for k, v in d.items():
    print(k, "occured", v, "times")     
    
'''
h occured 1 times
e occured 1 times
l occured 2 times
o occured 1 times
w occured 1 times
'''    
    