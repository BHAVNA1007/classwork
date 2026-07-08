#02_self_modifies_internal_state_of_obj

class Counter:
   def __init__(self):
       
       self.count = 0

    
   def increment(self):
       self.count += 1

   def decrement(self):
       self.count -= 1

   def display(self):
       return self.count

c = Counter()
c.increment()
c.increment()
print(c.display())
c.decrement()
print(c.display())