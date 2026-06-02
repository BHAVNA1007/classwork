#04_reverse_each_row

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


# mannualy reverse 

for row in matrix:
   i = 0
   j = len(row) - 1
   while i < j:
      temp = row[i]
      row[i] = row[j]
      row[j] = temp    
      i += 1
      j = j-1

print("\nmatrix after revers:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=' ')
    print()

'''
# using reverse():
for rowww in matrix:
     rowww.reverse()

print("reverse matrix: ")

for i in range(rows):
    for j in range(cols):
       print(matrix[i][j],end=" ")
    print()
'''

'''
#using slicing here actual matrix can change and print:
for roww in matrix:
    print(roww[::-1])
'''



