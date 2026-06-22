#03_tuple_inside_list_sorting

students = [('deepika',30),('vaibhav',15),('virat', 35)]
s1 = sorted(students)
print(s1) #[('deepika', 30), ('vaibhav', 15), ('virat', 35)]


s2 = sorted(students, key=lambda student:student[1])
print(s2) #[('vaibhav', 15), ('deepika', 30), ('virat', 35)]

