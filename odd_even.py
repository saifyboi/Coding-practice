import cmath
#check odd even based on user input
a = int(input("Enter a number: "))
odd = a % 2
if odd==0:
   print(f"{a} is even")
else:
    print(f"{a} is odd")
