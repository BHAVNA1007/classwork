#06_words_count


linecount = 0
wordcount = 0

with open("app.log", "r") as file:
   
    for line in file:
       if line.strip():

          linecount += 1

          wordcount += len(line.split())

print("total lines ", linecount)
print("total word count ", wordcount)

print("line and word count is done")



'''
total lines  16
total word count  21
line and word count is done
'''




'''
#after adding ------>>>>> if line.strip():  blank lines skip

total lines  6
total word count  21
line and word count is done
'''


