#03_random

#random()

import random

#print(dir(random))


print(random.random()) #0.5432004252891673


print(random.uniform(10,20)) #13.43893271766554

print(random.randrange(1,10,2)) #3

#choice()

names= ["rash","deep","virat"]

print(random.choice(names))
'''
deep
virat
'''

print(random.choices(names, k=2)) 
'''
['deep', 'rash']
['virat', 'virat']
'''

cards =[1,2,3,4,5]
random.shuffle(cards)
print(cards)


number = random.randint(1,10)
guess  = int(input("number: "))

if guess == number:
   print("wow...")
else:
   print("wrong")

 


