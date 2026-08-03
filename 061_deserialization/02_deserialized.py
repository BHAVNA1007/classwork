#02_deserialized


import pickle

file = open("student1.dat", "rb")

s1 = pickle.load(file)

file.close()

print(s1)

print(s1['name'])

print("object deserealized....")



'''
{'id': 101, 'name': 'bhavna', 'course': 'pyhton'}
bhavna
object deserealized....
'''