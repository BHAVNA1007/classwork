#03_3D_Array

a =[[[1,2],
     [2,3]],
    [[4,5],
     [6,7]]]

print(a)
print(len(a))
print(len(a[0]))


for i in range(len(a)):
    print("layer",i)
    for j in range(len(a[i])):
       for k in range(len(a[i][j])):
          print(a[i][j][k], end=' ')
       print()
    print()
