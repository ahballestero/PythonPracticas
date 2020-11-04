import tkinter as tk
from tkinter import Button

window = tk.Tk() #declaro variable 'window' y llamo a tkinter
window.geometry("640x480") #Doy tamaño a la ventana

button1=tk.Button(window, text="Boton 1")
button2=tk.Button(window, text="Boton 2")
button3=tk.Button(window, text="Boton 3")


button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)


#def saludo(name):
#    print("Hola " + name)

#textbox=tk.Entry(window)
#textbox.pack()

#label=tk.Label(window)
#label.pack()

#def userinput():
#    ui=textbox.get()   #funcion para copiar lo que escribo en la caja de texto y mostrarlo luego en la consola
#    label["text"] = ui

#button1=tk.Button(window, text="Dale aquí", command=userinput)
#button1.pack()




#label=tk.Label(window, text="Etiqueta de pruebas", bg="cyan")
#label.pack(fill=tk.BOTH, expand=True) #Para que se muestre en la ventana y colocar el elemento


#importante no poner parentesis a la función
#button1=tk.Button(window, text="Dale aqui", command=lambda: saludo("humano")) 
#button1.pack()





window.mainloop() #Esto mantiene la ventana sin cerrar (siempre al final)