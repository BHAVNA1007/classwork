#03_students_subjects_chapers
'''
stu = 1
while stu <= 3:
   
   print("Student",stu,end=" ")

   sub = 1
   while sub <= 5:
   
        print(f"\nSubject{sub}:",end=" ")
        
        chp = 1
        while chp <= 4:
            print(f"Chapter{chp}",end=" ") 
            chp += 1
           

        sub += 1
        print()

   stu += 1 
   print() 
        
        
 '''

'''
count = 0
for s in range(1, 4):
    print("Student",s,end=" ")
    for sub in range(1,6):
        print("\nSubject",sub,end=" ")
        for chp in range(1,5):
            count+=1 
            print("Chapter",chp,end=" ")
        print()
    print()               
      
print(count)  

'''

for s in range(1,4):
    print("Student",s,end=" ")  
   
    sub = 1
    while sub<=5:

        print("Subject",sub,end=" ") 
         
        sub += 1
    print()

    
