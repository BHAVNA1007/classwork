#06_methods

# keys()
student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)
print(student.keys())  # dict_keys(['name', 'age', 'city'])

print(list(student.keys()))  # ['name', 'age', 'city']

print(set(student.keys()))  # {'city', 'name', 'age'}

# values()
student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)
print(student.values())  # dict_values(['dipu', 30, 'chennai'])

print(list(student.values()))  # ['dipu', 30, 'chennai']

print(set(student.values()))  # {'chennai', 30, 'dipu'}

# items()
student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)
print(student.items())  #dict_items([('name', 'dipu'), ('age', 30), ('city', 'chennai')])

print(list(student.items()))  #[('name', 'dipu'), ('age', 30), ('city', 'chennai')]

print(set(student.items())) #{('city', 'chennai'), ('age', 30), ('name', 'dipu')}

student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)

for key, value in student.items():
    print(key,value)
    
# update()
student = {"name": "dipu", "age": 30, "city": "chennai"}

student.update({"salary": 50000})

student.update({"city": "indore"})

print(student) #{'name': 'dipu', 'age': 30, 'city': 'indore', 'salary': 50000}

# copy()
student = {"name": "dipu", "age": 30, "city": "chennai"}

s1 = student.copy()
print(s1)  # {'name': 'dipu', 'age': 30, 'city': 'chennai'}

s1.update({"salary": 90000})

print(s1)

print(student)    
    

    