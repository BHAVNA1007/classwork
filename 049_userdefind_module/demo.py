import mymath

print(mymath.add(10,20))
print(mymath.sub(50,5))


#using alias

import mymath as m
print(m.add(20,90))
print(m.sub(100,50))


import hello 
print(hello.PI)
print(hello.marks)

import hello as h
print(h.PI)
print(h.marks)


import employee as e
print(e.companyname)
print(e.calculatesalary(50000))


print(e.display())


from employee import display
from hello import display
display()


from hello import display
from employee import display
display()