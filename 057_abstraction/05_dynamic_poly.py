#05_dynamic_poly


class Bird:
   def fly(self):
      print("birds fly.....")

class Airplain:
   def fly(self):
       print("airplain fly.....")

objects = [Bird(), Airplain()]

for obj in objects:
    obj.fly()

'''
birds fly.....
airplain fly.....

'''