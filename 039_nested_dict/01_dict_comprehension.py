#01_dict_comprehension
se = {i : i*i for i in range(1,11) if i%2==0}

print(se) #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


words = {"dipu","thapaji","krishna"}
print(type(words))   #<class 'set'>
d = {word: len(word) for word in words}
print(d)    #{'krishna': 7, 'dipu': 4, 'thapaji': 7}
print(type(d))     #<class 'dict'>

numbers = [1,2,3,4,5]
r = {x: "even" if x%2==0 else "odd" for x in numbers}
print(r) #{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

keys = ["name","age","city"]
value = ["deepika", 30, "chennai"]
d ={keys[i]: value[i] for i in range(len(keys))}
print(d)   #{'name': 'deepika', 'age': 30, 'city': 'chennai'}
