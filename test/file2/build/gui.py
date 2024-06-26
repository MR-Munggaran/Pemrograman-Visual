
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Kampus\PEMVIS\test\file2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    100.0,
    fill="#000000",
    outline="")

canvas.create_text(
    83.0,
    411.0,
    anchor="nw",
    text="Label 2 ISAN",
    fill="#000000",
    font=("Inter SemiBold", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    697.5,
    431.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=498.0,
    y=407.0,
    width=399.0,
    height=46.0
)

canvas.create_text(
    83.0,
    282.0,
    anchor="nw",
    text="Label 1 ISAN",
    fill="#000000",
    font=("Inter SemiBold", 36 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    697.5,
    306.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=498.0,
    y=282.0,
    width=399.0,
    height=46.0
)

canvas.create_text(
    83.0,
    153.0,
    anchor="nw",
    text="File ISAN",
    fill="#000000",
    font=("Inter SemiBold", 36 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    697.5,
    173.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=498.0,
    y=149.0,
    width=399.0,
    height=46.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1157.0,
    y=153.0,
    width=226.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1157.0,
    y=282.0,
    width=226.0,
    height=48.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1157.0,
    y=407.0,
    width=226.0,
    height=48.0
)

canvas.create_rectangle(
    70.0,
    512.0,
    691.0,
    937.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    762.0,
    512.0,
    1383.0,
    937.0,
    fill="#D9D9D9",
    outline="")
window.resizable(False, False)
window.mainloop()
