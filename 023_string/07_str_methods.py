#07_str_methods

#01  upper()
a = "welcome"
print(a.upper())
a = "weLcome"
print(a.upper())


#02 lower()
a = "WELCome"
print(a.lower())


#03 capitalize()
a = "hello guys how are u"
print(a.capitalize())


#04 title()
a = "hello guys how are u"
print(a.title())


#05 swapcase()
a = "Hello Guys How Are U"
print(a.swapcase())


#06 find()
a = "hello guys how the life is going on"
print(a.find('e'))
print(a.find('guys'))
print(a.find("hw"))


#07 rfind()
print(a.rfind('e'))
print(a.rfind('o'))


#08 index()
s = "deepika"
print(s.index('a'))
print(s.index('e'))


#09 rindex()
s = "deepikae"
print(s.rindex('a'))
print(s.rindex('e'))


#10 isalpha()
s = "deepikae"
print(s.isalpha())
print("rashmika123".isalpha())
print("123".isalpha())
print("$%#".isalpha())
print("heloo guys".isalpha())


#11 isdigit()
s = "deepika123"
print(s.isdigit())
print("123".isdigit())
print("#$@".isdigit())
print("123 456".isdigit())


#12 isalnum()
s = "deepika123"
print(s.isalnum())
print("123".isalnum())
print("#$@".isalnum())
print("123 456".isalnum())
print("abc".isalnum())


#13 islower()
s = "deepika123"
print(s.islower())
print("123".islower())
print("#$@".islower())
print("123 456".islower())
print("abc".islower())
print("ABC".islower())


#13 isupper()
s = "deepika123"
print(s.islower())
print("123".isupper())
print("#$@".isupper())
print("123 456".isupper())
print("abc".isupper())
print("ABC".isupper())



#14 isspace()

s = "deepika123"
print(s.isspace())
print("123".isspace())
print("#$@".isspace())
print("123 456".isspace())
print("  ".isspace())
print("ABC".isspace())


#15 istitle()
print("Hwllo Gyus How Are You".istitle())
print("Hlloe gyus how are you".istitle())
print("Heloow guyS ".istitle())
print("Hwllo 123 Gyus How Are You".istitle())


#16 replace()
s= "i like python"
print(s.replace("python","JavaScipt"))


#17 strip()
s = "   python   "
print(s)
print(len(s))

s1 = s.strip()
print(len(s1))
print(s1)


#18 lstrip()
s = "   python   "
print(len(s))
print(s)
print(s.lstrip())

s1 = s.lstrip()
print(len(s1))
print(s1)


#19 rstrip()
s = "   java  "
print(s)
print(s.rstrip())


#20 splite()
s = "hello guys how are u"
print(s.split())

l1 =s.split()
print(l1)
print(len(l1))
print(l1[0])

s = "Hello,guys,how,are,you"
print(s.split())
l1 = s.split(',')
print(l1)
print(len(l1))
print(l1[0])



#21 join()
l1 = ['hello', 'guys', 'how', 'are', 'you'] 
print(" ".join(l1))
s1 = ' '.join(l1)
print(s1)
print(','.join(l1))




