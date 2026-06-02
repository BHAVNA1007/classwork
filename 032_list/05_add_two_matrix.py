#05_add_two_matrix
#print()  all for extra line

rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("ele.. for m1")
matrix1 = []
for i in range(rows):
    row = [] 
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row)
print() 

print("ele.. for m2")
matrix2 = []
for i in range(rows):
    row = [] 
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row)
print()

print("matrix1:")
for i in range(rows):
     for j in range(cols):
        print(matrix1[i][j],end=' ')
     print()   
print()   


print("matrix2:")
for i in range(rows):
     for j in range(cols):
        print(matrix2[i][j],end=' ')
     print() 
print()


#finally sum of two metrix:

matrix3 = []
for i in range(rows):
     row = []
     for j in range(cols):
         row.append(matrix1[i][j] + matrix2[i][j])           
     matrix3.append(row)

print("\nsum metrix3 is:")
for i in range(rows):
    for j in range(cols):
       print(matrix3[i][j],end=' ')
    print()

'''
#another approch using zero metrix

matrix3 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    matrix3.append(row)
print()

print("Zero metrix for storing sum ")
for i in range(rows):
   for j in range(cols):
       print(matrix3[i][j],end=' ')
   print()

for i in range(len(matrix1)):
    for j in range(len(matrix1[1])):
        matrix3[i][j] = matrix1[i][j]+matrix2[i][j]
   
print("sum of both metrix in matrix3 is:")
for i in range(rows):
    for j in range(cols):
        print(matrix3[i][j],end=" ")
    print()  
'''


