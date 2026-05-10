#01_if_inside_case

age = int(input("Enter The age : "))

match age:
     case x if x < 13:
          print("Child")  
     case x if x < 20:
          print("Teen")
print("Out of match case ")
  