r1 = int(input("Rows: "))
c1 = int(input("Columns: "))

print("ele for m1...")
matrix1 = []

for i in range(r1):
     row = []
     for j in range(c1):
          row.append(int(input()))
     matrix1.append(row)
print()

r2 = int(input("Rows: "))
c2 = int(input("Columns: "))

print("ele for m1...")
matrix2 = []

for i in range(r2):
     row = []
     for j in range(c2):
          row.append(int(input()))
     matrix2.append(row)
print()

if c1!=r2:
   print("multiplication not possible")

else:
    res = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        res.append(row) 
   
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] = res[i][j] + matrix1[i][k] * matrix2[k][j]

   
    print("\nMatrix1: ")
    for i in range(r1):
        for j in range(c1):
            print(matrix1[i][j],end=' ')
        print() 

    print("\nMatrix2: ")
    for i in range(r2):
        for j in range(c2):
            print(matrix2[i][j],end=' ')
        print() 
    print("\nResult: ")
    for row in res:
        print(row)   
      

  