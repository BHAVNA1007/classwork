#04_iterate_on_each

students = {

101 : {"name": "dipu", "age": 30},
102 : {"name": "virat", "age": 35}

}

students[103] = {"name": "rashmika", "age": 30}

for k, v in students.items():
    print("ID", k)
    for k1, v1 in v.items():
        print(k1, "=", v1)        

'''
ID 101
name = dipu
age = 30
ID 102
name = virat
age = 35
ID 103
name = rashmika
age = 30
'''

company = {
"emp1" : {"name": "deepika", "skills": ["python", "java"]},
"emp2" : {"name": "virat", "skills": ["python", "react"]}
}
print(company)

'''
{'emp1': {'name': 'deepika', 'skills': ['python', 'java']}, 'emp2': {'name': 'virat', 'skills': ['python', 'react']}}
'''

response = {
"user" : {
"id" : 101,
"profile": {"name": "dipu", "email": "d@gmail.com"}
}
}
print(response["user"]["profile"]["email"])  #d@gmail.com