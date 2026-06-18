#03_odd_even_using_lambda

l1 = [10,20,31,32]

r = map(lambda a:"even" if a%2==0 else "odd",l1)
print(list(r)) #['even', 'even', 'odd', 'even']


#grad

l1 = [92,60,31,56]

r = map(lambda x:"A" if x>90 else "B" if x>70 else "C" if x>60 else "D" if x>50 else "Fail", l1 )
print(list(r))
