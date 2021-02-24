from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("La misteriosa ventana sin nombre")

mivar = StringVar()


frame = Frame(root, width=1000, height=550)

frame.pack()

nombre = Label(frame, text="Nombre: ")
nombre.grid(row=0, column=0, sticky="w")

text1 = Entry(frame)
text1.grid(row=0, column=1,padx=4, pady=3)

lastname = Label(frame, text="Apellidos: ")
lastname.grid(row=1, column=0, sticky="w")

text2 = Entry(frame)
text2.grid(row=1, column=1, pady=3)

passw = Label(frame, text="Contraseña: ")
passw.grid(row=2, column=0, sticky="w")

text4 = Entry(frame)
text4.grid(row=2, column=1, pady=3)
text4.config(show="*")

email = Label(frame, text="E-mail: ")
email.grid(row=3, column=0, sticky="w")

text3 = Entry(frame)
text3.grid(row=3, column=1, pady=3)

coment = Label(frame, text="Comentarios: ")
coment.grid(row=4, column=0, sticky="w")

textcom = Text(frame)
textcom.grid(row=4, column=1, pady=3)
textcom.config(width=15,height=10)

def prueba():
    messagebox.showinfo("Prueba", text1.get())

sendButton = Button(frame,text="Enviar", command=prueba)
sendButton.grid(row=5,column=1,sticky="e")


vertScroll=Scrollbar(frame, command=textcom.yview)
vertScroll.grid(row=4,column=2,sticky="nsew")

textcom.config(yscrollcommand=vertScroll.set)




root.mainloop()
