#07_copy_deepcopy

student = {"name": "dipu", "age": 30, "city": "chennai", "marks": [87, 66]}
print(student)

s1 = student.copy()
print(s1)  # {'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}

s1["marks"][0] = 77
print(student)  # {'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66]}
print(s1)  # {'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66]}



import copy
student = {"name": "dipu", "age": 30, "city": "chennai", "marks": [87, 66]}

#case 1
s1 = student
print(s1)

#case 2
s1 = student.copy()
print(s1) #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}

#case 3
s1 = copy.deepcopy(student)
print(s1)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}

s1.update({"new": "areee"})
s1["marks"][0] = 90

print(student)
print(s1) #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [90, 66], 'new': 'areee'}

