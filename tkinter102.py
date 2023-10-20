from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text="Submit", command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title="Application Completed", message="Submission successful!")
if __name__ == "__main__":
    root = MyGui()
    root.pack()
    root.mainloop()