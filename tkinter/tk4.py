from tkinter import *

def submit():
    username = entry.get()
    print("hello " + username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

submit = Button(window,text="submit",command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Ink Free',50))
entry.config(bg='black')
entry.config(fg='green')
# entry.insert(0,'yoyo')
# entry.config(show='*')

entry.pack()

window.mainloop()