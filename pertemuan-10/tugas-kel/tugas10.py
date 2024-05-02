from tkinter import *
from kubus import RotatingCubeApp
from prisma import PrismaApp
from bola import MovingBallApp

def create_rotating_cube_app():
    root = Tk()
    app = RotatingCubeApp(root)
    root.mainloop()

def create_prisma_app():
    root = Tk()
    app = PrismaApp(root)
    root.mainloop()

def create_ball_app():
    root = Tk()
    app = MovingBallApp(root)
    root.mainloop()

top = Tk()
top.geometry("300x300")
B = Button(top, text="3D Kubus", command=create_rotating_cube_app)
C = Button(top, text="3D Prisma", command=create_prisma_app)
D = Button(top, text="3D Bola", command=create_ball_app)
B.place(x=125, y=125)
C.place(x=125, y=90)
D.place(x=125, y=50)
top.mainloop()
