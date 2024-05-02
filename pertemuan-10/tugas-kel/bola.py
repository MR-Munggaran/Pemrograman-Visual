import tkinter as tk
import math

class MovingBallApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Moving Ball")

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.angle_x = 0
        self.angle_y = 0
        self.rotation_speed_x = 0.05  # Kecepatan rotasi horizontal
        self.rotation_speed_y = 0.05  # Kecepatan rotasi vertikal

        self.draw_ball()
        self.rotate_ball()

    def draw_ball(self):
        # Hapus objek bola yang lama
        self.canvas.delete("ball")

        # Define bola
        ball_center = [200, 200]
        ball_radius = 50

        # Hitung posisi titik-titik pada bola
        points = []
        num_points = 100
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = ball_center[0] + ball_radius * math.sin(self.angle_y) * math.cos(angle)
            y = ball_center[1] + ball_radius * math.sin(self.angle_x) * math.sin(angle)
            points.append([x, y])

        # Gambar bola
        self.canvas.create_polygon(points, fill="lightblue", outline="black", tags="ball")

    def rotate_ball(self):
        # Perbarui sudut rotasi
        self.angle_x += self.rotation_speed_x
        self.angle_y += self.rotation_speed_y

        # Gambar bola dengan rotasi baru
        self.draw_ball()

        # Panggil metode ini lagi setelah 20 milidetik
        self.master.after(20, self.rotate_ball)

    def set_rotation_speed(self, speed_x, speed_y):
        self.rotation_speed_x = speed_x
        self.rotation_speed_y = speed_y