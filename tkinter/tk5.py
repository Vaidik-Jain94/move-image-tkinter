from tkinter import *

def display():
    if (x.get()==1) & (y.get()==0):
        print("I like python")
    elif (x.get()==0) & (y.get()==1):
        print("I like java")
    elif (x.get()==1) & (y.get()==1):
        print("i like both")
    else:
        print("i don't like either")

window = Tk()

x = IntVar()
y = IntVar()

checkbox = Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20))
checkbox.config(fg='yellow')
checkbox.config(bg='black')
checkbox.config(activebackground='black')
checkbox.config(activeforeground='yellow')
photo = PhotoImage(file='tkinter/python_logo.png')
photo = photo.subsample(8)
checkbox.config(image=photo,compound='left')
checkbox.config(padx=25,pady=20,width=250,height=50)
checkbox.config(anchor='w')

checkbox2 = Checkbutton(window,text='Java',variable=y,onvalue=1,offvalue=0,command=display)
checkbox2.pack()
checkbox2.config(font=('Arial',20))
checkbox2.config(fg='yellow')
checkbox2.config(bg='black')
checkbox2.config(activebackground='black')
checkbox2.config(activeforeground='yellow')
photo2 = PhotoImage(file='tkinter/java_logo.png')
photo2 = photo2.subsample(16)
checkbox2.config(image=photo2,compound='left')
checkbox2.config(padx=25,pady=40,width=250,height=50)
checkbox2.config(anchor='w')

window.mainloop()