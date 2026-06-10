# del operation

students = {

101 : {"name": "dipu", "age": 30},
102 : {"name": "virat", "age": 35},
103 : {"name": "dipuiiiiiiiii", "age": 39},
104 : {"name": "viratiiiiiiiii", "age": 50}

}
print(students)

del students[101]
'''
{102: {'name': 'virat', 'age': 35}, 103: {'name': 'dipuiiiiiiiii', 'age': 39}, 104: {'name': 'viratiiiiiiiii', 'age': 50}}
'''
'''
print(students[101])
KeyError: 101
'''
print(students)

print(students[102].pop("name")) #virat
print(students)
print(students[102].pop("name", "NOT FOUND")) #NOT FOUND


print(students[104].popitem()) #('age', 50)
print(students)  #{102: {'age': 35}, 103: {'name': 'dipuiiiiiiiii', 'age': 39}, 104: {'name': 'viratiiiiiiiii', 'age': 50}}

print(students[103].clear())    #None
print(students)  #{102: {'age': 35}, 103: {}, 104: {'name': 'viratiiiiiiiii'}}

