#05_calculator

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
op = input("Enter The Operators (+, -, *, /, %) = ")

match op:
     case "+":
        print("Sum of two number = ", num1+num2)
     case "-":
        print("Subtraction of two numbers =", num1-num2)
     case "*":
        print("multiplication of two numbers =", num1*num2)
     case "/":
         if num2!=0:
            print("division of two numbers =", num1/num2)
         else:
            print("avoid Zero")
     case "%":
          print("modulo of two numbers = ", num1%num2)
     case _:
          print("Provide valid operators")  

print("Exit from calculator...")