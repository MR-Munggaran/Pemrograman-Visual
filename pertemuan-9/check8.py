from tkinter import *

top = Tk()

## Membuat List Box

framelist = Frame(top)
framelist.pack()
Lb1 = Listbox(top)
Lb1.insert(1, 'python')
Lb1.insert(2,'perl')
Lb1.insert(3,'C')
Lb1.insert(4,'PHP')
Lb1.insert(5,'JSP')
Lb1.insert(6,'Ruby')

Lb1.pack()


## Membuat MenuButton
framebutt = Frame(top)
framebutt.pack()
mb = Menubutton(framebutt, text='condiments', relief=RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb['menu'] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label='mayo', variable=mayoVar)
mb.menu.add_checkbutton(label='ketchup', variable=ketchVar)
mb.pack()


## Membuat menu
def donothing():
    filewin = Toplevel(top)
    button = Button(filewin, text="Do nothing button")
    button.pack()

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)


## Membuat Message
framelabel = Frame(top)
framelabel.pack()

var = StringVar()
label = Message(framelabel, textvariable=var, relief=RAISED)
var.set("What Are you Doing?")
label.pack()


## Membuat Radio Button
def sel():
    selection = "you selected the option " + str(var.get())
    label.config(text = selection)

frameradio = Frame(top)
frameradio.pack()

var = IntVar()
R1 = Radiobutton(frameradio, text='Option 1', variable=var, value=1, command=sel)
R1.pack(anchor = W)
R2 = Radiobutton(frameradio, text='Option 2', variable=var, value=2, command=sel)
R2.pack(anchor = W)
R3 = Radiobutton(frameradio, text='Option 3', variable=var, value=3, command=sel)
R3.pack(anchor = W)
label = Label(top)
label.pack()

## MEmbuat Scale
def scal():
    selection = "Value = " + str(var.get())
    label.config(text = selection)

framescale = Frame(top)
framescale.pack()

var = DoubleVar()
scale = Scale(framescale, variable=var)
scale.pack(anchor=CENTER)

button = Button(framescale, text='Get Scale Value', command=scal)
button.pack(anchor=CENTER)

label= Label(top)
label.pack


top.mainloop()
