#02_passing_list_into_args

#way 01

list1 = [1,2,3,4,5]
def add(a,b,c,d,e):
   return a+b+c+d+e
print("way 01 adding elements sum is:",add(*list1)) 

#adding elements sum is:  15

#way 02
def add(*l1):
   s = 0
   for i in l1:
      s = s+i
   return s
print("way 02 adding elements sum is:",add(10,20,30,40,50))

#way 03
l1 =[10,20,30,40]
def add(*l2):
   return sum(l2)
print(add(*l1))  #100

#way 04
l1 =[10,20,30,40]
def add(l2):
   return sum(l2)
print(add(l1)) #100

