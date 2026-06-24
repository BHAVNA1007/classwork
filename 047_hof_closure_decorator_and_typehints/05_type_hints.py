#05_type_hints


'''
syntax:

def functionname(para1:type1, para2:type2)->returntype
    return somthing

'''


def add(a:int, b:int)->int:
    return a+b

result = add(5,10)
print(result)


'''
#python -m mypy 05_type_hints.py
def add(a:int, b:int)->int:
    return "hello"

result = add(5.5,"dipu")
print(result)

'''
 