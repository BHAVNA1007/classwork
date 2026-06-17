#04_with_positonal_arg_kwargs

def display(name, **details):
  print(name,details)
display("deepika", age=30, address="mumbai")

#deepika {'age': 30, 'address': 'mumbai'}

def profile(**info):
   if "name" in info:
      print("welcome", info["name"])

   if "email" in info:
      print("Email: ", info["email"])

   if "address" in info:
      print("Address: ", info["address"])

profile(name="deepika", email="dee@gmail.com", address="chennai")

'''
welcome deepika
Email:  dee@gmail.com
Address:  chennai
'''

