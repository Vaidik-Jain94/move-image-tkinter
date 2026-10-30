from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='this is info box',message='u r vaidik')
    # messagebox.showwarning(title='warning',message='u have virus')
    # messagebox.showerror(title='error',message='something went wrong')

    # if messagebox.askokcancel(title='ask ok cancel',message='do u want the thing'):
    #     print("u did the thing")
    # else:
    #     print("u didn't do the thing")

    # if messagebox.askretrycancel(title='ask retry cancel',message='do u want to retry'):
    #     print("u retried")
    # else:
    #     print("u didn't retry")

    # if messagebox.askyesno(title='ask yes no',message='do u like cake'):
    #     print("i like cake too")
    # else:
    #     print("i don't")

    # answer = messagebox.askquestion(title='ask question',message='do u like coding')
    # if (answer == 'yes'):
    #     print("i do")
    # else:
    #     print("i don't")

    answer = messagebox.askyesnocancel(title='ask yes no cancel',message='do u like coding',icon='question')
    if (answer == True):
        print("i do")
    elif (answer == False):
        print("i don't")
    else:
        print("you dodged the question")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()