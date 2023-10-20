import math

def qaudratic_eq():
    a = int(input("Please enter the 'a'co-eficients of your  qaudratic eq:"))
    b = int(input("Please enter the 'b'/co-eficients of your  qaudratic eq:"))
    c = int(input("Please enter the 'c'/co-eficients of your  qaudratic eq:"))
    d2 = math.pow(b, 2)
    d1 = 4*a*c
    x1 = ((-b) + (math.sqrt(d2 -d1))) / (2*a)
    x2 = ((-b) - (math.sqrt(d2 - d1))) / (2*a)
    print(f"The 1st root of x is: {x1}")
    print(f"The 2nd root of x is: {x2}")
#If I dont split the math functions, preference takes over eg sqrt  is  done b4 pow
qaudratic_eq()
#To make b^2 - 4ac > 0 fix the code!


