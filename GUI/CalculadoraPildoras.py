from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

large_font = ('Arial', 15)

digitoDisplay=StringVar()



display=Entry(miFrame, textvariable=digitoDisplay)

display.grid(row=1,column=1,columnspan=4,pady=5,padx=4)
display.config(bg="black",fg="#00db00",justify=RIGHT,width=14,font=large_font)

#-------------------------Pulsaciones teclas---------------------------------------------------------#

def pulsacionesTeclas(numPulsado):
    digitoDisplay.set(digitoDisplay.get() + numPulsado)



#-------------------------Primera fila---------------------------------------------------------#

boton7=Button(miFrame, text="7",width=5,height=2,command=lambda:pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8",width=5,height=2,command=lambda:pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9",width=5,height=2,command=lambda:pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)

botondiv=Button(miFrame, text="/",width=5,height=2)
botondiv.grid(row=2, column=4)


#-------------------------Segunda fila---------------------------------------------------------#

boton4=Button(miFrame, text="4",width=5,height=2,command=lambda:pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5",width=5,height=2,command=lambda:pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6",width=5,height=2,command=lambda:pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)

botonmult=Button(miFrame, text="x",width=5,height=2)
botonmult.grid(row=3, column=4)

#-------------------------Tercera fila---------------------------------------------------------#

boton1=Button(miFrame, text="1",width=5,height=2,command=lambda:pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2",width=5,height=2,command=lambda:pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3",width=5,height=2,command=lambda:pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)

botonrest=Button(miFrame, text="-",width=5,height=2)
botonrest.grid(row=4, column=4)

#-------------------------Cuarta fila---------------------------------------------------------#

boton0=Button(miFrame, text="0",width=5,height=2,command=lambda:pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)

botoncoma=Button(miFrame, text=",",width=5,height=2,command=lambda:pulsacionesTeclas("."))
botoncoma.grid(row=5, column=2)

botonigual=Button(miFrame, text="=",width=5,height=2)
botonigual.grid(row=5, column=3)

botonsuma=Button(miFrame, text="+",width=5,height=2)
botonsuma.grid(row=5, column=4)


raiz.mainloop()
