'''
10_read_r_c_from_user_nd_read_all_ele_from_user_nd_display_them

'''

rows = int(input('Enter the rows: '))
cols = int(input('Enter the columns: '))

matrix = []
for i in range(rows):
    rows = []
    for j in range(cols):
        rows.append(int(input()))
    matrix.append(rows)

print("ele... are")

for i in matrix:
   for j in i:
      print(j,end=' ')
   print()
