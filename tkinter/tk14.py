from tkinter import *

def openFile():
    print("You opened a file")

def saveFile():
    print("You saved a file")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editmenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

window.mainloop()