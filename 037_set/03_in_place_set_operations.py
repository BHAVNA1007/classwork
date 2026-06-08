#03_in_place_set_operations

#update()            |= 

s = {1,2,3}
c = {3,4,5}

s.update(c)
print(s)        #{1, 2, 3, 4, 5}
print(c)      #{3, 4, 5}

s = {1,2,3}
s.update({3,4},{5,6})
print(s)             #{1, 2, 3, 4, 5, 6}

s = {1,2,3}
c = {3,4,5}
s |= c
print(s)   #{1, 2, 3, 4, 5}

#intersection_update()          &=

s = {1,2,3}
c = {3,4,5}
s &= c
s.intersection_update(c)
print(s)     #{3}

#difference_update()     -=

s = {1,2,3}
c = {3,4,5}
s -= c
s.difference_update(c)
print(s)     #{1,2}

#symmetric_difference_update()     ^=

s = {1,2,3}
c = {3,4,5}
s ^= c
s.symmetric_difference_update(c)
print(s)     #{1, 2, 3}