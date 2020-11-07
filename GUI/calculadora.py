from tkinter import *

root=Tk()


frame=Frame(root)
frame.pack()

#Pantalla
numeroPantalla=StringVar()
screen=Entry(frame,textvariable=numeroPantalla)
screen.grid(row=1,column=1,columnspan=4,padx=10,pady=10)
screen.config(bg="black", fg="#03f943",justify=RIGHT)
#Fin pantalla

#Funcionalidades
def numeroPulsado(num):

    numeroPantalla.set(numeroPantalla.get()+num)




#Fin Funcionalidades

#Fila botones 1
button7=Button(frame,text="7",width=3,command=lambda:numeroPulsado("7"))
button7.grid(row=2,column=1)
button8=Button(frame,text="8",width=3,command=lambda:numeroPulsado("8"))
button8.grid(row=2,column=2)
button9=Button(frame,text="9",width=3,command=lambda:numeroPulsado("9"))
button9.grid(row=2,column=3)
buttonDiv=Button(frame,text="/",width=3)
buttonDiv.grid(row=2,column=4)
#Fin de fila botones 1

#Fila botones 2
button4=Button(frame,text="4",width=3,command=lambda:numeroPulsado("4"))
button4.grid(row=3,column=1)
button5=Button(frame,text="5",width=3,command=lambda:numeroPulsado("5"))
button5.grid(row=3,column=2)
button6=Button(frame,text="6",width=3,command=lambda:numeroPulsado("6"))
button6.grid(row=3,column=3)
buttonx=Button(frame,text="x",width=3)
buttonx.grid(row=3,column=4)
#Fin de fila botones 2

#Fila botones 3
button1=Button(frame,text="1",width=3,command=lambda:numeroPulsado("1"))
button1.grid(row=4,column=1)
button2=Button(frame,text="2",width=3,command=lambda:numeroPulsado("2"))
button2.grid(row=4,column=2)
button3=Button(frame,text="3",width=3,command=lambda:numeroPulsado("3"))
button3.grid(row=4,column=3)
buttonmin=Button(frame,text="-",width=3)
buttonmin.grid(row=4,column=4)
#Fin de fila botones 3

#Fila botones 4
button0=Button(frame,text="0",width=3,command=lambda:numeroPulsado("0"))
button0.grid(row=5,column=1)
buttoncom=Button(frame,text=",",width=3,command=lambda:numeroPulsado("."))
buttoncom.grid(row=5,column=2)
buttoneq=Button(frame,text="=",width=3)
buttoneq.grid(row=5,column=3)
buttonplus=Button(frame,text="+",width=3)
buttonplus.grid(row=5,column=4)


#Fin de fila botones 4




root.mainloop()