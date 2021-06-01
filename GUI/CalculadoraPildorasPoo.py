from tkinter import *
import regex

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

        boton7=self.colocar_boton(7)
        boton8=self.colocar_boton(8)
        boton9=self.colocar_boton(9)
        botondiv=self.colocar_boton("/")


        boton4=self.colocar_boton(4)
        boton5=self.colocar_boton(5)
        boton6=self.colocar_boton(6)
        botonx=self.colocar_boton(u"\u00d7")
        #botonx.config(text="x")


        boton1=self.colocar_boton(1)
        boton2=self.colocar_boton(2)
        boton3=self.colocar_boton(3)
        botonrest=self.colocar_boton("-")


        botoncero=self.colocar_boton(0)
        botoncoma=self.colocar_boton(".")
        botonigual=self.colocar_boton("=",mostrar=False)
        botonmas=self.colocar_boton("+")

        #Lista Botones

        botones=[boton7,boton8,boton9,botondiv,boton4,boton5,boton6,
        botonx,boton1,boton2,boton3,botonrest,botoncero,botoncoma,botonigual,botonmas]

        contador=0

        for fila in range(2,6):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
            

    def colocar_boton(self, valor, mostrar=True, ancho=6, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 10), command=lambda:self.pulsaciones_teclas(valor, mostrar))
        
    def pulsaciones_teclas(self, valor, mostrar):
        
        if mostrar:
            self.operacion+=str(valor)
            self.mostrar_pantalla(valor)
        
        elif not mostrar and valor=="=":
            self.operacion=regex.sub(u"\u00d7", "*", self.operacion)
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))
        
        else:
            pass

    def mostrar_pantalla(self, valor):
        self.display.insert(END,valor)

    def borrar_pantalla(self):
        self.display.delete(0,END)






        





mi_calculadora=Calculadora(raiz)


raiz.mainloop()

