#05_strftime


from datetime import datetime

now = datetime.now()
f = now.strftime("%Y-%m-%d")
print(f)

f = now.strftime("%y-%m-%d")
print(f)

f = now.strftime("%y-%B-%d")
print(f)

f = now.strftime("%H:%M:%S")
print(f)

f = now.strftime("%H:%M:%S: %p")  #19:58:36: PM
print(f)                  


f = now.strftime("%A")  #Friday
print(f)

f = now.strftime("%a")  #Fri
print(f)

f = now.strftime("%B")   # June
print(f)

f = now.strftime("%b")   # Jun
print(f)

f = now.strftime("%j")  # 177
print(f)

f = now.strftime("%w")   #5
print(f)

