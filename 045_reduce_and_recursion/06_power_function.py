#06_power_function

def pow(b,p):
  if p==0:
     return 1
  return b*pow(b,p-1)

def main():
  x = pow(2,5)
  print(x)

main()

#32