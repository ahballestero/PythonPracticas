from tkinter import *

root=Tk()

root.title("Ventana de pruebas")

#root.resizable(0,0) #También puede ser True o False

root.iconbitmap("/Users/ahbal/Desktop/Python/GUI/python.ico")

#root.geometry("1024x768")

root.config(bg="magenta")

miFrame=Frame()

miFrame.pack(side="right", anchor="n")

miFrame.config(bg="red")

miFrame.config(width="640", height="480")

root.mainloop()