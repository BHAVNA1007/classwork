#05_sum_of_n_natural_nums

def sum(n):
  if n == 0:
     return 0
  return n+sum(n-1)

def main():
   n = int(input("Enter N: "))
   x = sum(n)
   print(x)

main()