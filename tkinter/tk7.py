from tkinter import *

def submit():
    print("the temperature is : " + str(scale.get()) + " degree C")

window = Tk()

scale = Scale(window,
              from_ = 100,
              to = 0,
              length=600,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval=10,
              #showvalue=0,  # hides current value
              resolution=5,
              troughcolor='blue',
              fg='red',
              bg='black' )
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()