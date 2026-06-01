#04_peak_element

n = int(input('Enter the size: '))
print("plz enter ele...")

l = []
for i in range(n):
    l.append(int(input()))
print(l)


peakindex = -1
for i in range(n):
   if i == 0:
      if n==1 or l[i] >= l[i+1]:
         peakindex = i
         break
   elif i==n-1:
      if l[i] >= l[i-1] :
         peakindex = i
         break
   else:
      if l[i] >= l[i-1] and l[i] >= l[i+1]:
         peakindex = i
         break
if peakindex != -1:
    print('peak ele index is',peakindex, "and value is:",l[peakindex])

else:
    print("No peak element: ")

