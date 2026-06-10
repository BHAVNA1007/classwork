#03_modification


students = {

101 : {"name": "dipu", "age": 30},
102 : {"name": "virat", "age": 35}

}
print(students) #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 35}}

#modification in dict
students[102]["age"] = 60
print(students)  #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 60}}



# adding new student
students[103] = {"name": "rashmika", "age": 30}
print(students) 

'''{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 60}, 103: {'name': 'rashmika', 'age': 30}}'''