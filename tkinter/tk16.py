from tkinter import *

def create_window():
    # new_window = Toplevel()  # old window close kari toh dono close hongi
    new_window = Tk()
    window.destroy()  # it will close the old window

window = Tk()

Button(window,text="create new window",command=create_window).pack()

window.mainloop()