#04_3D_read_value_from_user

layer = int(input("Layer:"))
rows = int(input("Rows:"))
cols = int(input("Columns:"))


arr = []
for l in range(layer):
    print(f"\nLayer{l+1}") 

    matrix = []
    for r in range(rows):

        row = []
        for c in range(cols):

           value = int(input())
           row.append(value)

        matrix.append(row)

    arr.append(matrix)
print()

print("\n3D A array")
for l in range(layer):
    print(f"\nLayer{l+1}")

    for r in range(rows):
        for c in range(cols):
            print(arr[l][r][c], end=' ')
        print() 
              

