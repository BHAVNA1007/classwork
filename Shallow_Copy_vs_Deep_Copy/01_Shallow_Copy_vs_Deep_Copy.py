#01_Shallow_Copy_vs_Deep_Copy
'''
Shallow copy creates a new outer object but shares references 
to nested objects, whereas deep copy creates 
a completely independent copy of both the outer object and
 all nested objects.'''

#000000001. List with Immutable Elements
#Shallow Copy
import copy
a = [1,2,3]
b = a.copy()
b[0] = 100
print(a) #[1, 2, 3]
print(b) #[100, 2, 3]

#Deep Copy
c = copy.deepcopy(a)
c[0] = 200
print(a) #[1, 2, 3]
print(c) #[200, 2, 3]

#original list not changed in both case 
#reason: Integers are immutable.

#0000002. Nested List 
# Shallow Copy
a = [[1,2],[3,4]]
b = a.copy()
b[0][0] = 100
print(a) #[[100, 2], [3, 4]]
print(b) #[[100, 2], [3, 4]]
#Both point to same inner list.
'''When Python performs a shallow copy, 
it creates a new outer container, 
but the inner objects are not copied.'''

#Deep Copy.
# deepcopy() creates new outer objects and new inner objects.
#Only list C changes.
c = copy.deepcopy(a)
c[0][0] = 500
print(a)  #[[100, 2], [3, 4]]
print(c)  #[[500, 2], [3, 4]]
'''Because deep copy recursively creates completely new copies 
of all nested objects, so no references are shared.'''


#0000005. Tuple with Immutable Elements

a = (1,2,3)
b = copy.copy(a)
#b[0] = 100  TypeError: 'tuple' object does not support item assignment
print(a) #(1, 2, 3)
print(b)  #(1, 2, 3)

c = copy.deepcopy(a)
print(a)  #(1, 2, 3)  Same object returned
print(c)   #(1, 2, 3)   Same object returned


