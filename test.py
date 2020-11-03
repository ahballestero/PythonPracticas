from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def multiplicar():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")

# Configuración de la raíz
root = Tk()
root.config(bd=20)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Multiplicar", command=multiplicar).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()