import tkinter as tk

def fun1(event):
    label.config(text="Haha")
def fun2(event):
    label.config(text="Label1")

root=tk.Tk()
label=tk.Label(root,text="Label1")
label.grid(row=1,column=1)
label.bind("<Enter>", fun1)
label.bind("<Leave>", fun2)
root.mainloop()