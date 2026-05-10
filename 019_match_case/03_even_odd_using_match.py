#03_even_odd_using_match

a = int(input("Enter The Choice = "))
match a%2:
    case 0:
        print("even")
    case 1:
        print("odd")
    case _:
        print("wrong choice")
print("out of match case") 