#02_sorting_in_lambda

numbers = [5,2,8,6,7]
a = sorted(numbers)
print(a)  #[2, 5, 6, 7, 8]


b = sorted(numbers, reverse=True)
print(b)  #[8, 7, 6, 5, 2]

x = sorted(numbers, key = lambda x:x)
print(x)  #[2, 5, 6, 7, 8]

names =['hi','bye','deepika', 'rashmika', 'ab']
a = sorted(names)
print(a) #['ab', 'bye', 'deepika', 'hi', 'rashmika']

b = sorted(names , reverse=True)
print(b)  #['rashmika', 'hi', 'deepika', 'bye', 'ab']

x = sorted(names, key=lambda x:len(x))
print(x) #['hi', 'ab', 'bye', 'deepika', 'rashmika']