from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = ball(canvas,0,0,100,1,1,"white")
tennis_ball = ball(canvas,0,0,50,3,7,"red")
base_ball = ball(canvas,0,0,140,15,8,"yellow")

while True:
    volley_ball.move()
    tennis_ball.move()
    base_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()