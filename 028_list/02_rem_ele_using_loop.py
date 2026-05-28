#02_rem_ele_using_loop
'''
#this appoch is wrong because it skipped some element when it # will left shifted :
a = [10,20,30,40]
for i in a:
    if i%2==0:
      a.remove(i)
print(a)
'''

'''
#so we have below solution:
#here we copied the original list using a[:]
a = [10, 20, 30, 40]
for i in a[:]:
   if i%2==0:
       a.remove(i)
print(a)  


a = [10, 21, 30, 41,43]
for i in a[:]:
   if i%2==0:
       a.remove(i)
print(a) 
'''

#if we want to delet specific value which is start with #specific latter then: 

a = ["abc","axy","www","rrr"]
for i in a[:]:
    if i.startswith('a'):
        a.remove(i)
print(a) 
    







