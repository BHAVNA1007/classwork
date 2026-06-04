#07_converting_tuple_into_list

t1 = (1,2,8)
print(t1) #(1, 2, 8)

l = list(t1)
print(l)  #[1, 2, 8]


t1 = (11,33,22)
print(t1)
print(sorted(t1)) #[11, 22, 33]


import sys
t1 = ("abc","xyz","www")
print(t1)
print(sys.getsizeof(t1)) #64


t1 =t1 = ("abc","xyz","www")
print(t1)
print(sys.getsizeof(t1)) 


t2 =("abc","xyz","www")
print(t2)
print(sys.getsizeof(t2)) 