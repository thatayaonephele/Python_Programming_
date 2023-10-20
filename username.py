
"""
A program to compute the usernames
for a computer system
def username_option_1():
    The 1st option is if we assume the user enter both 1st and last name
    :return:

    :return: 
    """

"""
pasword = ''
count = 7
full_name = str(input("Please enter your name: "))
delimeter = full_name.find(" ")
while count >= 0:
    last_name = full_name[delimeter + 1:]
    count -= 1
y = (full_name[0])
print(f"Your password is: {y}{last_name}")
username_option_1()
"""

"""
def username_option_2():
    The 1st option is if we assume the user enter both 1st and last name
    :return:
    pasword = ''
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    pasword += first_name[0]+ last_name[:7]
    print(f"Your password is: {pasword}")
username_option_2()
The 2nd option is if we assume the user enters 1st and last name individually
"""

#Program that converts a user given month (allowed values[1-12]) into a month abbreviation
#eg input 3 output Mar. Note: I could use list, dict, tuple, slicing.
"""
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
usr_input = 0
user_month_choice = int(input("Please enter a month in digit/integer format: "))
usr_input = (range(1,13))
i = 3
output_month = ""
while user_month_choice not in usr_input:
    print("The number entered is out of range")
else:
    for x in range(0, len(months) + 1):
        while i >= 0:
        output_month = months[user_month_choice:]
        i-= 1

print(f"The {user_month_choice} represents the month {output_month}",end="")


#The solution below is the closet to the actual solution
i = 0
b = 3
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

usr_input = int(input("Please enter a month you'd like to convert: "))
individual_month =''
for x in range(0,len(months),3):
    i+= 1
    if i == 3:
        continue
    else:
        a = x / 3
        if usr_input == a:
            print(f"The value{usr_input} in month abbreviations is: {months[x]}")

"""
#Revisit Chapter 5.2
A = "A"
b = 8364
c= 960
print(chr(b))
print(chr(c))
print(ord(A))

#NB: Make sure you include them in your e-leraning program