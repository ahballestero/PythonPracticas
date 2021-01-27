from random import randrange
from tkinter import *
from tkinter.messagebox import showinfo
import random


root = Tk()
root.title("Si o no?")
# root.iconbitmap("GUI\python.ico")

frame = Frame(root, width=800, height=600)
frame.grid()

label = Label(frame, text="Eres un pringao/a?", font="Arial 40")
label.grid(row=0, column=0, columnspan=4, pady=70)


def popup_showinfo():
    showinfo("Confirmado", "Sabia que eras un pringao/a! XD")


def randomizeno(e):
    random = randrange(-1, 300)
    button2.place(x=random, y=random)


button1 = Button(frame, text="SI", width=12, height=2, command=popup_showinfo)
button1.grid(row=9, column=1, padx=50, pady=10)


button2 = Button(frame, text="NO", width=12, height=2, command=randomizeno)
button2.grid(row=9, column=3, padx=50, pady=5)

button2.bind("<Enter>", randomizeno)

root.mainloop()
