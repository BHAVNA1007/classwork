#03_move_all_zeros_in_end

n = int(input('Enter the size: '))
print("plz enter ele...")

l = []
for i in range(n):
    l.append(int(input()))
print(l)

nonzeros = []
zeros = []
for i in l:
    if i == 0:
        zeros.append(i)
    else:
        nonzeros.append(i)

result =  nonzeros + zeros

print(result)