from tkinter import *
window = Tk()

photo = PhotoImage(file='tkinter/Cool_penguin_icon.png')

label = Label(window,
              text = "hello world",
              font=('arial', 40,'bold'),
              fg='green',  # text colour
              bg='black',
              relief=RAISED,  # border style
              bd=16,  # border size
              padx=20,  # padding left right
              pady=20,
              image=photo,
              compound='bottom')  # padding top down
label.pack()
# label.place(x=0, y=0)


window.mainloop()