#08


def test():
    try:
        return 10/0

    except ZeroDivisionError:
        return "error handled"

    finally:
        print("from finally")

    print("end of function") #this line not executed here

print(test())


'''
from finally
error handled

'''