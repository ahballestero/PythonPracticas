from tkinter import *

def construir_botones(self, botones, filas_botones):
    contador=0
    for fila in range(2,filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row=fila,column=columna)
            contador+=1
            

def colocar_boton(self, valor, mostrar=True, ancho=6, alto=2):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 10), command=lambda:self.pulsaciones_teclas(valor, mostrar))