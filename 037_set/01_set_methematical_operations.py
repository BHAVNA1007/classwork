#01_set_methematical_operations

#union()    |         

s1 = {1,2,3,4}
s2 = {3,4,6,7,8,9,9}

print(s1)    #{1, 2, 3, 4}
print(s2)      #{3, 4, 6, 7, 8, 9}
print(s1|s2)     #{1, 2, 3, 4, 6, 7, 8, 9}
print(s1.union(s2))     #{1, 2, 3, 4, 6, 7, 8, 9}

sports = {"thapa", "aman"}
culture = {"krishna","kuldeep","aman"}

print(sports)         #{"thapa", "aman"}
print(culture)          # {"krishna","kuldeep","aman"}

print(sports|culture)   #{'kuldeep', 'aman', 'krishna', 'thapa'}
print(sports.union(culture))   #{'kuldeep', 'aman', 'krishna', 'thapa'}

# intersection()       &

a  = {1,2,3}
b = {2,3,4,5,}

print(a&b)             #{2, 3}
print(a.intersection(b))     #{2, 3}

sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep"}

print(sports & culture)             #{'aman'}
print(sports.intersection(culture))        #{'aman'}

# difference()    -

a = {1,2,3}
b = {2,4}

print(a-b)    #{1, 3}
print(a.difference(b))   #{1, 3}

print(b-a)    #{4}
print(b.difference(a))    #{4}

#note: a-b not equal to b-a

sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep"}

print(sports - culture)              #{'thapa'}
print(sports.difference(culture))         #{'thapa'}


#symmitric difference           ^

sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep"}

print(sports ^ culture)              #{'thapa', 'krishna', 'kuldeep'}
print(sports.symmetric_difference(culture))     #{'thapa', 'krishna', 'kuldeep'}


# issubset()  <=

sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep"}

print(sports <= culture)       #False      
print(sports.issubset(culture))     #False


sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep","thapa"}

print(sports <= culture)       #True
print(sports.issubset(culture))        #True


# issuperset()   >=

sports = {"thapa","aman"}
culture = {"krishna", "aman", "kuldeep","thapa"}

print(culture  >= sports )       #True
print(culture .issuperset(sports))        #True


# isdisjointset

s = {1,2}
c = {3,4}
print(s.isdisjoint(c))     #True









