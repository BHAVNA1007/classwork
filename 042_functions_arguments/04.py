#04
'''
def evenlist(n):
    evens = []
    for i  in range(1, n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

def main():
    print("welcome")
    print(evenlist(10))    
    x = evenlist(10)
    print(type(x))
main()
'''    
'''
[2, 4, 6, 8, 10]
<class 'list'>
'''
def evenlist(n):
    return n  
def main():
    print("welcome")
    x = evenlist([10,20,30,40])
    print(x)
    print(type(x))
main()    
'''
welcome
<class 'list'>
'''