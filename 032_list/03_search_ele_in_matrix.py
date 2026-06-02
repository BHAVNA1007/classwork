#03_search_ele_in_matrix

rows = int(input("Rows: "))
cols = int(input("Cols: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("matrix: ")


for i in range(rows):
    for j in range(cols):
       print(matrix[i][j],end=" ")
    print()

search = int(input("Enter ele: "))
flag = 0
for i in matrix:
    for j in i:
       if  j == search:
           flag = 1
           break
if flag  == 0:
    print("Banada not found")

           