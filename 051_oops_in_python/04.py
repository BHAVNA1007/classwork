#04

class Addition:
    def set(self, a, b):
        print("set is called...")
        self.a = a
        self.b = b
    
    def add(self):
        print("add is called...")
        self.c = self.a + self.b
 
    def display(self):
        print("display is called...")
        #print("final result: ", self.c)
        return self.c

a1 = Addition()
a1.set(10,20)   
a1.add()
#a1.display()
result = a1.display()
print(result)

'''
set is called...
add is called...
display is called...
30
'''


