from tkinter import *

root=Tk()
root.title("Ventana de pruebas")

root.resizable(0,0)

root.iconbitmap("/Users/ahbal/Desktop/Python/GUI/python.ico")

#root.geometry("650x350") #el tamaño de la raiz se adapta al frame, no hace falta darle un tamaño

#root.config(bg="red")

fr=Frame() #Creamos un frame
fr.pack() #Lo empaquetamos dentro de la raiz

fr.config(width="650",height="350")

root.mainloop() #Esto debe ir siempre al final para mantener el bucle

