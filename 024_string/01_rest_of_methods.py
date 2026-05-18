#01_join()

word = ['java','python','is','esay']
print(' '.join(word))
str =' '.join(word)
print(type(str))



# rsplit()
str ="python java react AI aree samjhe"
res = str.split(' ',2)
res1 = str.rsplit(' ',2)
print(res)
print(res1)


#center()
str ='python is language'
print(len(str))
print(str.center(20))
str1 = str.center(20)
print(len(str1))
print(str.center(20,"*"))
print(str.center(40,"*"))


#ljust()
str = 'python'
print(str.ljust(20))
print(str.ljust(20,"*"))


#rjust()
print(str.rjust(20))
print(str.rjust(20,"*"))



#dir()
str = 'python'
print(dir(str))
print(len(dir(str)))



#startwith()
str = 'python is nice language'
print(str.startswith("python"))
print(str.startswith('ppy'))



#endswith()
str = "python is nice language"
print(str.endswith('python'))
print(str.endswith('language'))



#format()
name = 'bahubali'
age = 40
#we can write it using three types
print('my name is {} and age is {} years'.format(name,age))

print('first name :{1}, second:{0}'.format('java','python'))

print('name is : {name},age is:{age}'.format(name="bahu",age=30))



#sorted()
str = "bahubali"
print(sorted(str))
result = "".join(sorted(str))
print(result)











