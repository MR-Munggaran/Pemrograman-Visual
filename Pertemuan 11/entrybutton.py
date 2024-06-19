from tkinter import *

print('=============== Mencetak dadta dari Entry Widget dengan Button')

root = Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root,width = 20)
entry1.pack()

Button(root, text = "cetak data",  command = CetakData).pack()

root.mainloop()