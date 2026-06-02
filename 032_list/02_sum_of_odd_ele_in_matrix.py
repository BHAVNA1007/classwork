#02_sum_of_odd_ele_in_matrix

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

sum = 0
for i in matrix:
    for j in i:
      if j % 2 != 0:
         sum = sum + j 
print("sum of all odd num is: ",sum)


'''
#another approach: 
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 != 0:
            sum = sum +matrix[i][j]

print(sum)
'''