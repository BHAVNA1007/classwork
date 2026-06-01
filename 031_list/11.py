#11

rows = int(input('rows are: '))
cols = int(input('columns are: '))

matrix = []

for i in range(rows):
    rows = []
    for j in range(cols):
        rows.append(int(input()))
    matrix.append(rows)


sum = 0
for i in  range(len(matrix)):
    for j in range(len(matrix[i])):
       sum = sum + matrix[i][j]
       j += 1
    i += 1
print("SUM IS: ",sum)