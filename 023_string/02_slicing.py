#02_slicing
#syntax:  (string[start : end : step ])


s1 = "hello world"

print(s1[0:5])


print(s1[6:11])


print(s1[6:14])

print(s1[ :5])

print(s1[6: ])

print(s1[1:10:2])

s2 ="heyyy guys heow are u"

print(s1[::2])

print(s1[-5])
print(s1[-8])
print(s1[:-4])


s3 = "welcome home"
print(s3[::-1])
print(s3)


s4 = "welcome"
r = s4[::-2]
print(s4)
print(r)



s5 = input("enter the string: ")
if s5 == s5[::-1]:
    print('pelindrom')
else:
    print("non pelindrom")

