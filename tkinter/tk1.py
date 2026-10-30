from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("my first GUI code")

icon = PhotoImage(file='tkinter/Cool_penguin_icon.png')
window.iconphoto(True,icon)
window.config(background="black")  # to make changes

window.mainloop()  # to display window