#03_menu_driven

while True:

   print("Menu")
   print("1 Add two numbers:")
   print("2 check even or odd:")
   print("3 exit")
   choice = int(input("Enter the choice:"))
   match choice:
        case 1:
           a = int(input("Enter first number:"))
           b = int(input("Enter second number:"))
           print("Sum is:", a+b)
        case 2:
           a = int(input("Enter a number:"))
           if a%2==0:
               print("even")
           else:
               print("odd")
        case 3:
           a = int(input("Enter a number:")) 
           print("Square:",a**2)     
        case 4:
              print("Exit")
              break