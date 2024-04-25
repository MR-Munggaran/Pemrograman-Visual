from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("300x300")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=125,y=125)
top.mainloop()

# =====================================

