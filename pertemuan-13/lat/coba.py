from tkinter import *
from tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_columns


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.winfo_toplevel().title('Data Viewer')
        
        # Create and place labels
        self.l1 = Label(self.master, text="File Name:")
        self.l2 = Label(self.master, text="X Label:")
        self.l3 = Label(self.master, text="Y Label:")
        
        self.l1.grid(row=0, column=0, sticky=W, pady=5)
        self.l2.grid(row=1, column=0, sticky=W, pady=5)
        self.l3.grid(row=2, column=0, sticky=W, pady=5)

        # Create and place entry widgets with larger width
        self.eFname = Entry(self.master, width=60)
        self.eXname = Entry(self.master, width=60)
        self.eYname = Entry(self.master, width=60)

        self.eFname.grid(row=0, column=1, padx=5, pady=5)
        self.eXname.grid(row=1, column=1, padx=5, pady=5)
        self.eYname.grid(row=2, column=1, padx=5, pady=5)

        # Create and place text widgets with larger size
        self.txtX = Text(self.master, width=40, height=15)
        self.txtY = Text(self.master, width=40, height=15)

        self.txtX.grid(row=3, column=0, rowspan=2, padx=5, pady=5, sticky=N)
        self.txtY.grid(row=3, column=1, rowspan=2, padx=5, pady=5, sticky=N)

        # Configure the style for buttons
        self.style = Style()
        self.style.map('D.TButton', foreground=[('pressed', 'red'), ('active', 'green')], background=[('pressed', 'black'), ('active', 'white')])

        # Create and place buttons with larger width
        self.btn_graph = Button(self.master, text="Show Regression Graph", style="D.TButton", command=self.show_graph, width=30)
        self.btn_graph.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        self.btn_stats = Button(self.master, text="Show Stats", style="D.TButton", command=self.show_stats, width=30)
        self.btn_stats.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        self.quit = Button(self.master, text="Quit", style="D.TButton", command=self.master.destroy, width=30)
        self.quit.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def show_graph(self):
        regression_plot(self.eFname.get(), self.eXname.get(), self.eYname.get())

    def show_stats(self):
        xstats, ystats = stats_columns(self.eFname.get(), self.eXname.get(), self.eYname.get())
        self.txtX.delete('1.0', END)
        self.txtY.delete('1.0', END)
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)

root = Tk()
root.geometry("800x600")  # Set the initial size of the window
app = Application(master=root)
app.mainloop()