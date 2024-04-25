import tkinter

top = tkinter.Tk()

c = tkinter.Canvas(top, bg="salmon", height=500, width=400)
coord = 10, 50, 240, 210
arc = c.create_arc(coord, start=0, extent=150, fill="red")

c.pack()
top.mainloop()