import tkinter as tk

root = tk.Tk()

Frameku = tk.Frame(root, bg = 'green')
Frameku.place(relwidth = 0.8, relheight = 0.8)

# root.mainloop()

Tombolku =  tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'white')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg = 'blue')
Entryku.pack()

root.mainloop()

from tkinter import *

root = Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width = 20); entry1.pack()
Button(root, text="Cetak Data", command=CetakData).pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        frame1 = tk.Frame(self.root)
        frame1.grid()
        frame2 = tk.Frame(frame1)
        frame2.grid(row=0, column=0)
        frame3 = tk.Frame(frame1)
        frame3.grid(row=1, column=0)

        self.FirstNum = tk.StringVar()
        self.SecondNum = tk.StringVar()
        self.Hasil = tk.StringVar()

        self.lblFirstNum = tk.Label(frame2, text='Masukkan bilangan pertama')
        self.lblFirstNum.grid(row=0, column=0)

        self.txtFirstNum = tk.Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = tk.Label(frame2, text='Masukkan bilangan kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = tk.Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = tk.Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = tk.Entry(frame2, textvariable=self.Hasil)
        self.txtHasil.grid(row=2, column=1)

        self.btnJumlahkan = tk.Button(frame3, text="Jumlahkan", command=self.Jumlahkan)
        self.btnJumlahkan.grid(row=2, column=0)
        self.btnReset = tk.Button(frame3, text="Reset", command=self.Reset)
        self.btnReset.grid(row=2, column=1)
        self.btnKeluar = tk.Button(frame3, text="Keluar", command=self.root.destroy)
        self.btnKeluar.grid(row=2, column=2)

    def Jumlahkan(self):
        try:
            pertama = float(self.FirstNum.get())
            kedua = float(self.SecondNum.get())
            hasil = pertama + kedua
            self.Hasil.set(str(hasil))
        except ValueError:
            messagebox.showerror('Error', 'Masukkan angka yang valid')

    def Reset(self):
        self.FirstNum.set('')
        self.SecondNum.set('')
        self.Hasil.set('')


if __name__ == '__main__':
    root = tk.Tk()
    application = DataInOut(root)
    root.mainloop()

#AskInteger
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("100x100")


def show():
    num = askinteger("Input", "Input an Integer")
    print(num)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()

#AskFloat
from tkinter.simpledialog import askfloat
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    num = askfloat("Input", "Input a floating point number")
    print(num)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()

#AskString
from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    name = askstring("Input", "Enter you name")
    print(name)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()

#AskOpenFile
from tkinter.filedialog import askopenfile
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    filename = askopenfile()
    print(filename)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()

#SimpleDialog
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
   ["Fulan",26,3000000],
   ["Fulanah",31,5600000],
   ["Fulani",21,2500000],
   ["Fulanu",24, 2700000],
]
index=0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("umur", "gaji")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Nama')
tree.heading('umur', text='Umur')
tree.heading('gaji', text='Gaji')

read_data()
root.mainloop()