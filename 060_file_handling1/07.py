#07

try:

   with open("marks.txt", "r") as f:

      total = 0
      count = 0
      hmarks = -1
      topper = ""

      for line in f:

          parts = line.strip().split()

          if not parts:
             continue

          name = parts[0]
          marks = int(parts[1])

          total += marks
          count += 1

          if marks > hmarks:
             hmarks = marks
             topper = name
     
      avg = total / count
      print("Highest marks", hmarks) 
      print("avg: ", avg)
      print("Topper ", topper) 

except FileNotFoundError as e:
     print(e)




'''
Highest marks 90
avg:  85.33333333333333
Topper  Bhavna
'''