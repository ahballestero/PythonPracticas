import tkinter as tk
from tkinter import Label
from tkinter.constants import BOTH, LEFT, RIGHT

root=tk.Tk()
root.geometry("320x200")
root.title("Si o no?")


label=tk.Label(root, text="Eres tontito?", font="Hack 20")

label.pack()


button1=tk.Button(root, text="SI")
button1.pack(side=LEFT, ipadx=5, ipady=5)
button2=tk.Button(root, text="NO")
button2.pack(side=RIGHT,ipadx=5, ipady=5)





#button1.grid(row=0, column=0)
#button2.grid(row=15, column=0)









root.mainloop()




