#02_multiple_choice_in_one_case

a = int(input("Enter the choice = "))
match a:
    case 0:
       print("zero")
    case 1:
       print("one")
    case 2|3|4:
       print("two three four")
    case _:
       print("wrong choice")
print("out of match case")

   