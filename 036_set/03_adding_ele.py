#03_adding_ele

s = {10,20,30,10,40}
print(s)  #{40, 10, 20, 30}
s.add(90)
print(s)  #{40, 10, 20, 90, 30}



#adding multiple elements

s = {10,20,30,10,40, 50}
print(s)    #{50, 20, 40, 10, 30}
s.update([3,4,5,6])
print(s)  #{3, 4, 5, 6, 10, 20, 30, 40, 50}