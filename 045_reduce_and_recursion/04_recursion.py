#04_recursion   factorial of 5 is 120

def fact(n):
   if n == 1:
      return 1
   return n*fact(n-1)

def main():
  x = fact(5)
  print(x)

main() 

