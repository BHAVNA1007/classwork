#06_table_between_two_numbers


x = int(input("Enter First Number = "))
y = int(input("Enter Second Number = "))

for n in range(x, y+1):
      
      i = 1
      while i<11:
           print(n*i, end=" ")
           i += 1
      print()