from pathlib import Path
from tkinter import *
from tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_columns


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Kampus\PEMVIS\test\file2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.winfo_toplevel().title('Data Viewer')
        self.master.geometry("1440x1024")
        self.master.configure(bg="#FFFFFF")
        
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1440.0,
            100.0,
            fill="#000000",
            outline=""
        )
        
        self.canvas.create_text(
            83.0,
            411.0,
            anchor="nw",
            text="Label 2",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )
        
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            697.5,
            431.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(  # Use tkinter.Entry instead of ttk.Entry
        )
        self.entry_1.place(
            x=498.0,
            y=407.0,
            width=399.0,
            height=46.0
        )
        
        self.canvas.create_text(
            83.0,
            282.0,
            anchor="nw",
            text="Label 1",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )
        
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            697.5,
            306.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
        )
        self.entry_2.place(
            x=498.0,
            y=282.0,
            width=399.0,
            height=46.0
        )
        
        self.canvas.create_text(
            83.0,
            153.0,
            anchor="nw",
            text="File",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )
        
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            697.5,
            173.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
        )
        self.entry_3.place(
            x=498.0,
            y=149.0,
            width=399.0,
            height=46.0
        )
        
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            command=self.show_graph,
        )
        self.button_1.place(
            x=1157.0,
            y=153.0,
            width=226.0,
            height=48.0
        )
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            command=self.show_stats,
        )
        self.button_2.place(
            x=1157.0,
            y=282.0,
            width=226.0,
            height=48.0
        )
        
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            command=self.master.destroy,
        )
        self.button_3.place(
            x=1157.0,
            y=407.0,
            width=226.0,
            height=48.0
        )
        
        self.canvas.create_rectangle(
            70.0,
            512.0,
            691.0,
            937.0,
            fill="#D9D9D9",
            outline=""
        )
        
        self.canvas.create_rectangle(
            762.0,
            512.0,
            1383.0,
            937.0,
            fill="#D9D9D9",
            outline=""
        )
        
        self.txtX = Text(self.master, width=40, height=15)
        self.txtY = Text(self.master, width=40, height=15)
        
        self.txtX.place(x=70, y=512)
        self.txtY.place(x=762, y=512)
        
        self.master.resizable(False, False)
    
    def show_graph(self):
        regression_plot(self.entry_3.get(), self.entry_2.get(), self.entry_1.get())

    def show_stats(self):
        xstats, ystats = stats_columns(self.entry_3.get(), self.entry_2.get(), self.entry_1.get())
        self.txtX.delete('1.0', END)
        self.txtY.delete('1.0', END)
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)

root = Tk()
app = Application(master=root) 
app.mainloop()