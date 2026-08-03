#01_serialization

import pickle

student = {
   "id": 101,
   "name": "bhavna",
   "course" : "pyhton"
}

file = open("student1.dat", "wb")
pickle.dump(student, file)

file.close()
print("object serialized...")

'''
object serialized...
'''