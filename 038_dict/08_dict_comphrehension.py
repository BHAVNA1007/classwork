#08_dict_comphrehension

sq = {}

# normal way
for i in range(1,6):
    sq[i] = i*i
print(sq)     #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#usning dict comprehension

sq = {i : i*i for i in range(1,6)}
print(sq)   #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 
    