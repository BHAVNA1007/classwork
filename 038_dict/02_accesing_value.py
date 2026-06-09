#02_accesing_value

student = {"name" : "mahesh",
                  "age" :  33,
                  "city" : "hyderabad" }
print(student)  

print(student["name"])

print(student.get("name"))

print(student["city"])

print(student.get("age"))

'''
print(student["salary"])   #KeyError: 'salary'

'''

print(student.get("salary"))  #None

# saffer way if key not exists

print(student.get("address","NOT FOUND"))