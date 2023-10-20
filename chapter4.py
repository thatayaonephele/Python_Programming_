#Graphical User Interface
import tkinter as tk
import turtle
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)

        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone!")
        for x in range(4):
            turtle.forward(100)
            turtle.right(90)
root = tk.Tk()
app = Application(master=root)
app.mainloop()