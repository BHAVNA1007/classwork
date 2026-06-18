#01_sq_using_lambda

n = [2,4,6,7,8]

r = map(lambda a:a*a, n)
print(list(r))   #[4, 16, 36, 49, 64]



#using normal and map
l = ["yogita","vaishnavi","thapaji","deepesh"]

def convert(a):
    return a.capitalize()
r = map(convert,l)
print(list(r))   #['Yogita', 'Vaishnavi', 'Thapaji','Deepesh']


#using lambda 
l = ["yogita","vaishnavi","thapaji","deepesh"]
r = map(lambda a:a.capitalize(),l)
print(list(r)) #['Yogita', 'Vaishnavi', 'Thapaji','Deepesh']

#conversion into upper case
l = ["yogita","vaishnavi","thapaji","deepesh"]
r = map(lambda a:a.upper(),l)
print(list(r)) #['YOGITA', 'VAISHNAVI', 'THAPAJI', 'DEEPESH']

#find len 
l = ["yogita","vaishnavi","thapaji","deepesh"]
r = map(lambda a:len(a), l)
print(list(r))  #[6, 9, 7, 7]


