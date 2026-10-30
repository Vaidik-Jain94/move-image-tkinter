# from tkinter import *

# def click():
#     print("Hello")

# window = Tk()

# button = Button(window, text="click me")
# button.config(command=click)
# button.config(font=('Ink Free',50,'bold'))
# button.config(bg='black')
# button.config(fg='#fcc603')
# button.config(activebackground='#fcc603')
# button.config(activeforeground='black')
# button.pack()

# image = PhotoImage(file='tkinter/Cool_penguin_icon.png')
# button.config(image=image)
# button.config(compound='bottom')
# # button.config(state=DISABLED)

# window.mainloop()


# PROJECT TIME

from tkinter import *

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    label2.pack()

window = Tk()

button = Button(window, text="click me")
button.config(command=click)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='black')
button.config(fg='#fcc603')
button.config(activebackground='#fcc603')
button.config(activeforeground='black')

image = PhotoImage(file='tkinter/Cool_penguin_icon.png')
button.config(image=image)
button.config(compound='bottom')
# button.config(state=DISABLED)

label = Label(window, text=count)
label.config(font=('Monospace', 50))
label.config(compound='top')
label.pack()
button.pack()
label2 = Label(window, image=image)

window.mainloop()