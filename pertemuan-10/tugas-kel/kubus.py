import tkinter as tk
import math

class RotatingCubeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rotating Cube")

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.angle_x = 0
        self.angle_y = 0
        self.rotation_speed = 0.05  # Kecepatan rotasi

        self.draw_cube()
        self.rotate_cube()

    def draw_cube(self):
        # Hapus objek kubus yang lama
        self.canvas.delete("cube")

        # Define cube vertices
        vertices = [
            [-50, -50, -50],  # front top left
            [50, -50, -50],   # front top right
            [50, 50, -50],    # front bottom right
            [-50, 50, -50],   # front bottom left
            [-50, -50, 50],   # back top left
            [50, -50, 50],    # back top right
            [50, 50, 50],     # back bottom right
            [-50, 50, 50]     # back bottom left
        ]

        # Rotate cube vertices around X axis
        rotated_vertices_x = []
        for vertex in vertices:
            x, y, z = vertex
            y_rotated = y * math.cos(self.angle_x) - z * math.sin(self.angle_x)
            z_rotated = y * math.sin(self.angle_x) + z * math.cos(self.angle_x)
            rotated_vertices_x.append([x, y_rotated, z_rotated])

        # Rotate cube vertices around Y axis
        rotated_vertices_xy = []
        for vertex in rotated_vertices_x:
            x, y, z = vertex
            x_rotated = x * math.cos(self.angle_y) - z * math.sin(self.angle_y)
            z_rotated = x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
            rotated_vertices_xy.append([x_rotated, y, z_rotated])

        # Project 3D vertices to 2D points
        projected_points = []
        for vertex in rotated_vertices_xy:
            x, y, z = vertex
            # Perspective projection
            distance = 200
            f = distance / (distance - z)
            x_projected = x * f
            y_projected = y * f
            projected_points.append([x_projected, y_projected])

        # Draw cube edges
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 0],  # front face
            [4, 5], [5, 6], [6, 7], [7, 4],  # back face
            [0, 4], [1, 5], [2, 6], [3, 7]   # connections
        ]

        for edge in edges:
            p1 = projected_points[edge[0]]
            p2 = projected_points[edge[1]]
            self.canvas.create_line(p1[0] + 200, p1[1] + 200, p2[0] + 200, p2[1] + 200, fill="black", tags="cube")

    def rotate_cube(self):
        # Perbarui sudut rotasi
        self.angle_x += self.rotation_speed
        self.angle_y += self.rotation_speed

        # Gambar kubus dengan rotasi baru
        self.draw_cube()

        # Panggil metode ini lagi setelah 20 milidetik
        self.master.after(20, self.rotate_cube)

    def set_rotation_speed(self, speed):
        self.rotation_speed = speed
