'''#import tkinder
import tkinter as tk
#create a varabile
root = tk.Tk()
# imput value
root.title("WEBSITE")
root.geometry("500x700")
root.config(bg="red")
#mainloop
root.mainloop()'''
from ctypes import windll, HRESULT
from idlelib.run import manage_socket
from msilib.schema import CheckBox
from random import expovariate
from tkinter import Label, mainloop, Entry, Button, Canvas, Message, StringVar
from tkinter.messagebox import askyesno

#3
'''
import tkinter as tk
from tkinter import Frame, mainloop, Button

root = tk.Tk()

root.title("WEBSITE")
root.geometry("500x700")
root.config(bg="yellow")
frame1 = Frame(root, width=300, height= 300, cursor="dot",  )
frame2 = Frame(root, width=300, height=300,cursor="dotbox" )
button1 = Button(frame1, text="Button1", bg="blue")
button2 = Button(frame2, text="Button2", bg="red")
button3 = Button(frame1, text="logged", fg="green")
frame1.pack(side="top")
frame2.pack(side="bottom")
button1.pack()
button2.pack()
button3.pack()
mainloop()
'''
#4
'''
import tkinter as tk
window = tk.Tk()

window.title("LOGIIN")
label1 = Label(window, text="Email")
label2 = Label(window, text="Password")

entry1 = Entry(window, width=40, borderwidth=5)
entry2 =  Entry(window, width=40, borderwidth=5)

label1.grid(row=0, column=1)
label2.grid(row=1,column=1)
entry1.grid(row=0, column=2)
entry2.grid(row=1, column=2)
mainloop()'''

#5 pack
'''
import tkinter as tk

window = tk.Tk()
window.title("website")
window.geometry("500x700")
window.config(bg="black")
label1 = Label(window, text="Top",bg="Red" , fg="white")
label2 = Label(window, text="left", bg= "blue", fg="white")
label3 = Label(window, text="right", bg="green", fg="white")
label4 = Label(window, text="botton", bg="pink", fg="white")
label1.pack(side="top", fill="x" , expand= False )
label2.pack(side="left", fill="y", expand=False)
label3.pack(side="right", fill="y", expand=False)
label4.pack(side="bottom", fill="x", expand=False)
mainloop()
'''
#6 button
'''
import tkinter as tk
window = tk.Tk()
window.title("button")
window.geometry("500x700")
def log_in():
    print("Logged In")
button1 = Button(window, text="log in", width=14, bg="Red",fg="white", activebackground="Black", activeforeground="White",command=log_in, font="blod")

button1.pack()
mainloop()
'''

#7 menu bar
'''
from tkinter import *

import tkinter as tk


window = tk.Tk()

menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label = "New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="exit", command= window.quit)
menu.add_cascade(label="File", menu= file)
window.config(menu= menu)
mainloop()
'''

#8 message box
'''
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

tkinter.messagebox.showerror("info", "Outside file")
question = tkinter.messagebox.askyesno("wheather", "it will rain")

if question == True:
    print("Take a car")
else:
    print("no it will not rain")

mainloop()
'''

#9 Drawing
'''
import tkinter as tk

window = tk.Tk()

c = Canvas(window, width=500, height=500)
c.pack()
c.create_line(0,0,500,500, fill="red", dash=(3,3), width=5)
c.create_line(0,500,500,0, fill="green", dash=(3,3), width=5)
c.create_rectangle(150,120,450,375, width=5, fill="red", outline="yellow")
mainloop()
'''

#10 message box
'''
import tkinter as tk

window = tk.Tk()
window.geometry("500x700")
var = StringVar()
entry_var = StringVar()
def insert():
    result = entry_var.get()
    var.set(result)

message = Message(window, textvariable= var , relief= 'raised' , padx=50, pady=50)
entry = Entry(window, textvariable=entry_var)
button = Button(window, text="OK" , command=insert)
message.pack()
entry.pack()
button.pack()

mainloop()
'''
#11 check box
'''
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")

check_box1 = Checkbutton(window, text="Car", width=10, height= 2, onvalue=1, offvalue=0)
check_box1.pack()
mainloop()
'''

#12 place
'''
import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

button = Button(window, text="button")
button.place(x = 200 , y=200)
mainloop()
'''
















