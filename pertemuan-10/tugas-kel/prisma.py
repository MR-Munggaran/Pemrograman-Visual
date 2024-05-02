import tkinter as tk
import math

class PrismaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Prisma")

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.angle = 0
        self.rotation_speed = 0.05  # Kecepatan rotasi

        self.draw_prisma()
        self.rotate_prisma()

    def draw_prisma(self):
        # Hapus objek prisma yang lama
        self.canvas.delete("prisma")

        # Define prisma vertices
        vertices = [
            [100, 100],  # A
            [300, 100],  # B
            [350, 200],  # C
            [250, 300],  # D
            [50, 200]    # E
        ]

        # Rotate prisma vertices
        rotated_vertices = []
        for vertex in vertices:
            x, y = vertex
            # Menghitung rotasi terhadap titik tengah prisma
            rotated_x = (x - 250) * math.cos(self.angle) - (y - 200) * math.sin(self.angle) + 250
            rotated_y = (x - 250) * math.sin(self.angle) + (y - 200) * math.cos(self.angle) + 200
            rotated_vertices.append([rotated_x, rotated_y])

        # Draw prisma faces
        # Draw front face
        self.canvas.create_polygon(rotated_vertices[0][0], rotated_vertices[0][1],
                                    rotated_vertices[1][0], rotated_vertices[1][1],
                                    rotated_vertices[2][0], rotated_vertices[2][1],
                                    rotated_vertices[3][0], rotated_vertices[3][1],
                                    fill="lightblue", outline="black", tags="prisma")

        # Draw back face
        self.canvas.create_polygon(rotated_vertices[0][0], rotated_vertices[0][1],
                                    rotated_vertices[1][0], rotated_vertices[1][1],
                                    rotated_vertices[4][0], rotated_vertices[4][1],
                                    fill="lightgreen", outline="black", tags="prisma")

        # Draw side faces
        self.canvas.create_polygon(rotated_vertices[0][0], rotated_vertices[0][1],
                                    rotated_vertices[4][0], rotated_vertices[4][1],
                                    rotated_vertices[3][0], rotated_vertices[3][1],
                                    fill="lightyellow", outline="black", tags="prisma")

        self.canvas.create_polygon(rotated_vertices[1][0], rotated_vertices[1][1],
                                    rotated_vertices[2][0], rotated_vertices[2][1],
                                    rotated_vertices[3][0], rotated_vertices[3][1],
                                    fill="lightcoral", outline="black", tags="prisma")

    def rotate_prisma(self):
        # Perbarui sudut rotasi
        self.angle += self.rotation_speed

        # Gambar prisma dengan rotasi baru
        self.draw_prisma()

        # Panggil metode ini lagi setelah 20 milidetik
        self.master.after(20, self.rotate_prisma)

    def set_rotation_speed(self, speed):
        self.rotation_speed = speed