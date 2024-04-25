import tkinter
 
root = tkinter.Tk()

Frameku = tkinter.Frame(root, bg="blue")
Frameku.place(relwidth=0.8, relheight=0.8)

Tombolku = tkinter.Button(Frameku, text="Pencet Aku", bg="white", fg="red")
Tombolku.pack()

Entryku = tkinter.Entry(Frameku, bg="green")
Entryku.pack()

root.mainloop()

