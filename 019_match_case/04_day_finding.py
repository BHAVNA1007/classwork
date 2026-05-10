#04_day_finding

day = input("Enter The day = ").lower()

match day:
    case "monday":
        print("start working day")
    case "sunday":
        print("its holiday!!!!!!!")
    case _:
        print("normal working days")
print("out of loop")
