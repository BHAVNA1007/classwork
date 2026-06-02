#01_diagonal_sum_of_matrix_ele


rows = int(input("Rows: "))
cols = int(input("Cols: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("matrix: ")

#diagonal sum:


for i in range(rows):
    for j in range(cols):
       print(matrix[i][j],end=" ")
    print()

sum = 0 
for i in range(len(matrix)):
       sum = sum + matrix[i][i]
print("Diagonal: ", sum)


