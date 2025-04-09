import  tkinter as tk

from tkinter import *

window  = tk.Tk()
window.geometry("500x500")

e = Entry(window, borderwidth=5, width=60, )
e.place(x=25,y=10)

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))

b = Button(window, width=12 , text="7", command=lambda :click(7))
b.place(x=25, y=60)

b = Button(window, width=12 , text="8",command=lambda :click(8))
b.place(x=160, y=60)

b = Button(window, width=12 , text="9",command=lambda :click(9))
b.place(x=300, y=60)

b = Button(window, width=12 , text="4",command=lambda :click(4))
b.place(x=25, y=120)

b = Button(window, width=12 , text="5",command=lambda :click(5))
b.place(x=160, y=120)

b = Button(window, width=12 , text="6",command=lambda :click(6))
b.place(x=300, y=120)

b = Button(window, width=12 , text="1",command=lambda :click(1))
b.place(x=25, y=180)

b = Button(window, width=12 , text="2",command=lambda :click(2))
b.place(x=160, y=180)

b = Button(window, width=12 , text="3",command=lambda :click(3))
b.place(x=300, y=180)

def clear():
    e.delete(0, END)

b = Button(window, width=12 , text="clear", command= clear)
b.place(x=25, y=240)

b = Button(window, width=12 , text="0",command=lambda :click(0))
b.place(x=160, y=240)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "additional":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))


b = Button(window, width=12 , text="=", command= equal)
b.place(x=300, y=240)



#operators
def add():
    n1 = e.get()
    global math
    math = "additional"
    global i
    i = int(n1)
    e.delete(0,END)


b = Button(window, width=6 , text="+", command=add)
b.place(x=420 , y=60)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window, width=6 , text="-", command=sub)
b.place(x=420 , y=120)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window, width=6 , text="*", command=mult)
b.place(x=420 , y=180)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window, width=6 , text="/", command=div)
b.place(x=420, y=240)
mainloop()