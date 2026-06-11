#04_group_word_by_length

words = ["deepika", "rashmik","virat","abcd", "a", "b", "c"]

g = {}

for w in words:
    l = len(w)
    if l not in g:
        g[l] = []
    g[l].append(w)
print(g)    
    
