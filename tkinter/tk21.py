from tkinter import *

def dosomething(event):
    print("You did a thing : " + str(event.x) + "," + str(event.y))

window = Tk()

window.bind("<Button-1>",dosomething) # left click
window.bind("<Button-2>",dosomething) # scroll wheel
window.bind("<Button-3>",dosomething) # right click
window.bind("<ButtonRelease>",dosomething)
window.bind("<Enter>",dosomething)
window.bind("<Motion>",dosomething)

window.mainloop()