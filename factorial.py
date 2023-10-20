import  math
"""def factorial_cal():
    sum = 1
    my_factorial = int(input("Please enter an nth value to be factored: "))
    n = my_factorial
    factorial_list = []
    while my_factorial>= 1:
        factorial_list.append(my_factorial)
        my_factorial -= 1
    for x in factorial_list:
        sum = sum * x
    print(f"The factorical of {n} is: {sum}")
#factorial_cal()
#Random BodMath problem
#Chapter 3 Discussion:
#1):
#a 7.4
#b 5
#c 8 16.Follows BODMAS theorem
#d Undefined/error msg
#e 11
#f 9 27 Follows BODMAS theorem

#2)
#a
n = 3
r = 5
a = 3
b = 4
print((math.pow(n, 2) - 1) / 2) #c
print(4*math.pi*math.pow(r,2)) #d
print(math.sqrt(math.pow(r*math.cos(a),2) + math.pow(r*math.sin(b), 2)))
#m_gradient = y2 - y1 / x2 - x1 question e
#b
#c
#d
#e

for z in list(range(1,10,2)):
    print(" {}: {}".format(z, z**3))
print(z)
z = 25 // -7 #Floor on negative numbers rounds of to furthest negative whol number on line
print(z)


def food_price_per_cm(): #Exercise #2
    pizza_area = math.pow(r, 2) * math.pi
    pizza_price = float(input("Please enter the price of your pizza:"))
    x = round(pizza_price/pizza_area,2)
    print("The price of pizza per cm is: R{}".format(x))
food_price_per_cm()

#It would make more sense to know the price per unit weight eg 23/kg etc
#eg weave hair extensions, petrol prices,
#So basically a linkedin of prices and available stock?No, else wwe can be sabotaged
#The app would have to update regulary so that when stock is unavaible users know in less than 5mins
#I'd need a db for the available shit to be bought.. is None:
o = 0
h = 0
c = 0
H = 1.00794
C =  12.0107
O = 15.9994
molecular_weight = 0
molecular_item = input("Which element would you like to find its molecular mass?\n(Eg H2O, CH4): ")
for x in molecular_item:
    if x == "O" or x == "o":
        o = float(input("Please enter the number of oxygen atoms: "))
        break
    elif x == "C" or x == "c":
        c = float(input("Please enter the number of carbon atoms: "))
        break
        print("skfkjef")
    elif x == "H" or x == "h":
        h = float(input("Please enter the number of hydrogen atoms: "))
        break
    else:
        print("The dat you have entered cannot be understood, try again")
    molecular_weight += (o*O + c*C + h*H)
print(
        Atom   Weight
                (grams / mole)
        -------------------------
        H       {}
        C       {}
        O       {}
        The molecular weight of {} is: {} mols
        .format(molecular_item, molecular_weight))
# Make the code better by adding the actual weights of as seen on periodic table and user just enters the number of molecules instead of element weight
# eg enter molecule index & the number of molecules eg : o, 2 Or Na,1

# Then we switch up: eg What is the weight of water(H2O)?
# Its best you use a dictionary

#4 Speed of lightning

def lightning_speed(time_elapsed):
    speed_of_light = 1100
    distance = round(time_elapsed * speed_of_light / 5280,2 )
    print(f"The distance to the lightning strike when {time_elapsed} seconds lapses is {distance} miles")
lightning_speed(4)

#6  Function for finding the slope of 4 points
def find_slope():
    y1 = float(input("Please enter a y1 values[y1, y2]: "))
    y2 = float(input("Please enter a y2 values[y1, y2]: "))
    x1 = float(input("Please enter a x1 values[x1, x2]: "))
    x2 = float(input("Please enter a x2 values[x1, x2]: "))
    m_gradient = round(y2 - y1 / x2 - x1, 2)
    print(f"The gradient of the 2 points entered is :{m_gradient}")
find_slope()
#7
def distance_between_points():
    y1 = float(input("Please enter a y1 values[y1, y2]: "))
    y2 = float(input("Please enter a y2 values[y1, y2]: "))
    x1 = float(input("Please enter a x1 values[x1, x2]: "))
    x2 = float(input("Please enter a x2 values[x1, x2]: "))
    distance = round(math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y2 - y1,2))), 2)
    print(f"The distance between the 2 points ({x1},{y1}) & ({x2}, {y2}) is: {distance}")
distance_between_points()
#8# Ouput the value of the epact

def epact_func():
    year = int(input("Please enter a 4 digit year: "))
    C = year // 100
    x = (8 + (C // 4) - C + ((80 + 13) // 25) + 11*(year % 19)) % 30
    print(f. The Gregorian epact for the year {year} is {x}
    (the number of days between January
    1st and the previous new moon.)
    This value is used to figure out the date of Easter.)
epact_func()

#9
#Finding the lengh of a triangle
def triange_length():
    a = float(input("Please enter the length of side a of a triangle: "))
    b = float(input("Please enter the length of side b of a triangle: "))
    c = float(input("Please enter the length of side c of a triangle: "))
    s = (a + b + c) / 2
    area =round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)
    print(f'The area of a triangle with sides {a}, {b} and {c} is {area}m^2')
triange_length()

#10 Find the length of step ladders resting on a wall

def ladder_distance():
    degrees = float(input("Please enter the angle in degrees: "))
    height = float(input("Please enter the required height in metres(m)"))
    angle = (math.pi * degrees / 180)
    length =  height / math.sin(angle)
    print("The required height ({:.2f}m)for the ladder slanting at an angle of {:.2f}radians is {:.2f}m".format(height, angle, length))
ladder_distance()

#11 Finding the sum of nth natural numbers
def sum_of_n_natural_numbers():
    sum = 0
    n = int(input("Please enter a natural number 'n': "))
    x = n
    if x == 0:
        print(f"The sum of the nth value is 0")
    while n > 0:
        sum += n
        n -= 1
    print(f"The sum of the nth value {x} is {sum}")
    if x < 0:
        print("Sorry, n cannot be a negative value")
sum_of_n_natural_numbers()

#Finding the sum of cubic nth values

def find_nth_cubic_sum(): #Question 12
    sum = 0
    n = int(input("Please enter a natural number 'n': "))
    x = n
    if x == 0:
        print(f"The sum of the nth value is 0")
    while n > 0:
        sum += math.pow(n, 3)
        n -= 1
    print(f"The sum of the nth value {x} is {sum}")
    if x < 0:
        print("Sorry, n cannot be a negative value")
find_nth_cubic_sum()

#Q12 Programming Exercises: 
def volume_of_circle():
    r = int(input("please enter a radius value: "))
    v = round(4/3 * math.pi * math.pow(r, 3), 2) #1 Calculate Volume & SA:
    sa = round(4 * math.pi * math.pow(r, 2), 2)
    print("The volume of a circle with radius {} is {}m^3".format(r, v))
    print("The Surface Area of a circle with radius {} is {}m^2".format(r, sa))
volume_of_circle()


#13 Let user control input amount
def control_user_input():
    sum = 0
    count = int(input("How many items would you like to sum?: "))
    for x in range(count):
        y = int(input(f"Please enter value {x+1}: "))
        sum += y
    print(f"The sum of the {count} values is {sum}")
control_user_input()

#14Find the average of entered values:

def average_of_user_input():
    sum = 0
    count = int(input("How many items would you like to sum?: "))
    for x in range(count):
        y = int(input(f"Please enter value {x+1}: "))
        sum += y
    avg = round(float(sum / count),2)
    print(f"The average of the {count} values is {avg}")
average_of_user_input()

#15Approximate the value of pi using a series:

def pi_approximation():
    pi_approx = 0
    counter = 1 #Decides if we adding or subtracting on the series
    a = 4
    iterate = int(input("Please enter the number of iterations you'd like to compose: "))
    for x in range(1,iterate,2):
        if counter % 2 == 0:
            pi_approx -= a / x
        else:
            pi_approx += a / x
        counter += 1
    approx_diff = math.pi - pi_approx
    print(f"The approximation of pi using {iterate} iterations is {pi_approx}")
    print(f"The difference between pi function and my series is {approx_diff}")
pi_approximation()


#Question 16 Compute your own fibonnaci series code
def fibonacci_series():
    m = 1
    fib_sum = 0
    counter = 0
    temp = 0
    iterate = int(input("Please enter the number of iterations you'd like to compose: "))
    x = iterate
    while iterate >= counter:
        temp = m #for swapping variables
        fib_sum += temp
        m += 1 #keeps track of the actual value at the iteration
        iterate -= 1 #Keeps track of loop
    print(f"The nth Fibonacci number for n = {x} is {m}")
fibonacci_series()


#Question 17
def newtons_method():
    z = float(input("Please enter the value to find the square root of (x)"))
    y = int(input("Please enter the number of times to improve the guess"))
    for x in range(y):
        guess = float(input("Please enter a guess for the root value of x: ")) #The current guessed value
        guess = guess + z/guess / 2
    print(f"The guess for the root value of {z} is {guess}")
newtons_method()
#Finish this tonight
"""
