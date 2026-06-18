#04_filter_function

l1 = [92,60,31,56,77,43]

def fun(x):
   return x%2==0

r = map(fun, l1)  
r1 = filter(fun, l1) 
print(list(r))   #[True, True, False, True, False, False]
print(list(r1))  #[92, 60, 56]


#using filter
l1 = [92,60,31,56,77,43]
r = filter(lambda x: x%2==0, l1)
print(list(r))   #[92, 60, 56]

# find start with m
l1 = ["deep","mashi","mahesh","mahi" ]
r = filter(lambda x:x.startswith("m"), l1)
print(list(r))  #['mashi', 'mahesh', 'mahi']

#find string length greater 5
l = ["rashmika","priyanka","mahi","sanu"]
r = filter(lambda a: len(a)>5,l)
print(list(r)) #['rashmika', 'priyanka']

# remove empty string way 1
l = ["sanu", " ", " ","ranu"]
r = filter(lambda x: x !=' ',l)
print(list(r)) #['sanu', 'ranu']

# remove empty string way 2
l = ["sanu", "", "","ranu"]
r = filter(lambda x: len(x)>0 ,l)
print(list(r)) #['sanu', 'ranu']

# remove empty string way 3
l = ["sanu", "", "","ranu"]
r = filter(lambda x:x ,l)
print(list(r)) #['sanu', 'ranu']


# suare num then find even squares
l1 = [10,20,31,40]
r = map(lambda a:a*a,l1)
r1 = filter(lambda r:r%2==0,r)
print(list(r1)) #[100, 400, 1600]

r = filter(lambda x:x%2==0, map(lambda x:x*x, l1))
print(list(r)) #[100, 400, 1600]

#resverse each word of list using map and lambda

l1 = ["ranu", "sanu", "priya"]

r1 = map(lambda x : x[::-1],l1)
print(list(r1))



