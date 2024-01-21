import math

#rectangle/square
def rectangle(a,b):
    c=a*b
    if a==b:
        print("area of square is:",c)
    else:
        print("area of rectangle is:",c)
    return c

print("enter length")
side1= int(input())
print("enter breadth")
side2= int(input())
rectangle(side1,side2)

#circle
def circle(a):
    b = math.pi*a**2
    print("area of circle is:", b)
    return b
print("enter radius")
r= int(input())
circle(r)
