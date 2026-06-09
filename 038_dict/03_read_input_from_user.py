#03_read_input_from_user

n = int(input("Enter number of students: "))
d = {}

i = 1
while i <= n:
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    d[name] = marks 
    i += 1
print("Name of student","\t","% of marks")

for x in d:
    print(x, "\t\t\t",d[x])     
