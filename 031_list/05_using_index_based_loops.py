#05_using_index_based_loops

a = [[10,20,30],
     [40,50,60],
     [70,80,90]]


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()



a = [[10,'deepika'],
     [40,50,60],
     [70],
     ['abc','xyz']]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()