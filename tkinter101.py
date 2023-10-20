import time
from tkinter import  *
from tkinter.messagebox import showinfo
from tkinter102 import  MyGui

"""import math
#Programming Exercises:
def volume_of_circle():
    r = int(input("please enter a radius value: "))
    v = round(4/3 * math.pi * math.pow(r, 3), 2) #1 Calculate Volume & SA:
    sa = round(4 * math.pi * math.pow(r, 2), 2)
    print("The volume of a circle with radius {} is {}m^3".format(r, v))
    print("The Surface Area of a circle with radius {} is {}m^2".format(r, sa))
volume_of_circle()"""

def reply():
    showinfo(title="Answer", message="Correct!")

root = Tk()
root.title("E-Learning")
button = Button(root, text="Check Ans", command=reply)
button.pack()
root.mainloop()