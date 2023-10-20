from tkinter import *
from tkinter102 import MyGui

main_window = Tk()    #main app window
main_window.title("True/False Section")
Label(main_window, text="Full Name:").pack()
pop_up_window = Toplevel() #pop Up window
Label(main_window, text="True").pack(side=LEFT)
Label(main_window, text="False").pack(side=RIGHT)
MyGui(pop_up_window).pack(side=RIGHT)
main_window.mainloop()
