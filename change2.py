
"""
#Practicising the left, right and centre justification
f_name = "Thati"
l_name = "Phele"
#print({0:0.2f} {1:0.2f} "is learning how to use format specifier".format(f_name,l_name))
print("Left justification:{0:<5}".format(f_name))

print("Right justification:{0:-5}".format(f_name))

"""
#A program that shows the precision of the float-point format specifier
def precision_of_fs():
    total = 107.56
    dollar_amount = total // 10
    cent_amount = total % 100
    print("{0:0.30f} {1:0.30f}".format(dollar_amount, cent_amount))
precision_of_fs()

#A program that converts cents into dollars
def change_2():
    total = 107.56
    dollar_amount = total // 10
    cent_amount = total % 100

    quarters
    dimes
    nickels
    pennies
    quarters * 25 + dimes * 10 + nickels * 5 + pennies