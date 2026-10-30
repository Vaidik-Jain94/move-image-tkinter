from tkinter import *

food = ["pizza","burger","hotdog"]

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered burger")
    elif(x.get()==2):
        print("you ordered hotdog")
    else:
        print("you ordered nothing")

window = Tk()

pizzaimg = PhotoImage(file='tkinter/pizza.png')
pizzaimg = pizzaimg.subsample(20)
burgerimg = PhotoImage(file='tkinter/burger.png')
burgerimg = burgerimg.subsample(26)
hotdogimg = PhotoImage(file='tkinter/hotdog.png')
hotdogimg = hotdogimg.subsample(12)
foodimg = [pizzaimg,burgerimg,hotdogimg]

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],
                              variable=x,  # grps buttons if they share the same variable
                              value=i,
                              padx = 25,
                              font=("Impact",50),
                              image = foodimg[i],
                              compound='left',
                              indicatoron=0,  # eliminet circle indicators
                              width=375,
                              command=order)
    radiobutton.pack(anchor=W)


window.mainloop()