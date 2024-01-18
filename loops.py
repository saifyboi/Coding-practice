#loops

'''
car = ["audi", "BMW", "Toyota"]
for x in car:
   if x <= "BMW":
      break
   print(x)
'''

#user input for while loop.
def user_input():
   while True:
      try:
         x = int(input("Enter a number:"))
         break
      except ValueError:
         print("Only intergers are accepted")
   return x

#y= cmath.sqrt(user_input()) 
      #OR
y= user_input()**0.5
print(f"The sq. rt of the number is {y}")
