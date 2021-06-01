from tkinter import *
import regex

from Botonera_Calculadora import *

raiz=Tk()

class Calculadora:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        self.iconbitmap="python.ico"
        self.operacion=operacion=""

        #Agregar Display
        
        self.display = Entry(ventana, font="Arial 15")

        #Ubicar Display
        
        self.display.grid(row=1, column=0, columnspan=4, pady=10)
        self.display.config(bg="black", fg="#00db00", justify="right",width=20, )

        #Creación de botones

        boton7=colocar_boton(self, 7)
        boton8=colocar_boton(self,8)
        boton9=colocar_boton(self, 9)
        botondiv=colocar_boton(self, "/")


        boton4=colocar_boton(self, 4)
        boton5=colocar_boton(self, 5)
        boton6=colocar_boton(self, 6)
        botonx=colocar_boton(self, u"\u00d7")
        #botonx.config(text="x")


        boton1=colocar_boton(self, 1)
        boton2=colocar_boton(self, 2)
        boton3=colocar_boton(self, 3)
        botonrest=colocar_boton(self, "-")


        botoncero=colocar_boton(self, 0)
        botoncoma=colocar_boton(self, ".")
        botonigual=colocar_boton(self, "=",mostrar=False)
        botonmas=colocar_boton(self, "+")

        #Lista Botones

        botones=[boton7,boton8,boton9,botondiv,boton4,boton5,boton6,
        botonx,boton1,boton2,boton3,botonrest,botoncero,botoncoma,botonigual,botonmas]

mi_calculadora=Calculadora(raiz)


raiz.mainloop()

