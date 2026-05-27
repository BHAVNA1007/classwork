#005_single_ele_updation_using_index

a =[10,20,30,40]
print(id(a))
a[1] = 100
print(a)
print(id(a))


a=[10,20,30,40]
a[-1] = 100
print(a)

'''
#index error occure here
a = [10,20,30,40]
a[-10] = 100
print(a)
'''

