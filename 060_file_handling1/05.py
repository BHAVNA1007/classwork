#05


with open("app.log", "r") as f:
  
   infocount = errorcount = warnningcount = totallines = 0

   for line in f:
    
       totallines += 1

       if "INFO" in line:
           infocount += 1

       elif "ERROR" in line:
           errorcount += 1

       elif "WARNING" in line:
           warnningcount += 1


print("summary")

print(totallines)

print(infocount)

print(errorcount)

print(warnningcount)