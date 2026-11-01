from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

xVelocity = 5
yVelocity = 3

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

backimage = PhotoImage(file='tkinter/burger.png')
backimage = backimage.subsample(8)
bimage = canvas.create_image(0,0,image=backimage,anchor=NW)

photoimage = PhotoImage(file='tkinter/pizza.png')
photoimage = photoimage.subsample(20)
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()

while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if(coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
            yVelocity = -yVelocity
    canvas.move(myimage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()