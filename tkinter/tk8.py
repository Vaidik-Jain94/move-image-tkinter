
def submit():

    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("you have ordered : ")
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='yellow',
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")
listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

frame = Frame(window)
frame.pack()

submitbutton = Button(frame,text="submit",command=submit)
submitbutton.pack(side=LEFT)

addbutton = Button(frame,text="add",command=add)
addbutton.pack(side=LEFT)

deletebutton = Button(frame,text="delete",command=delete)
deletebutton.pack(side=LEFT)

window.mainloop()