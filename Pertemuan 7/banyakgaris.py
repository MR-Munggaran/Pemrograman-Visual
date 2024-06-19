import numpy as np
import matplotlib.pyplot as plt

# titik
titik_garis = [
    (200, 100, 1000, 100),  # Garis horizontal
    (400, 200, 400, 900),   # Garis vertikal
    (600, 300, 800, 300)    # Garis horizontal
]

# Parameter untuk setiap garis (pd, lw, pr, pg, pb, lr, lg, lb)
parameter_garis = [
    (8, 8, 255, 0, 255, 0, 255, 255),  # Garis horizontal
    (8, 8, 255, 0, 255, 0, 255, 255),  # Garis vertikal
    (8, 8, 255, 0, 255, 0, 255, 255)   # Garis horizontal
]

# setting the size of the canvas
col = 2050
row = 2040

# Function untuk membuat garis
def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = pd // 2
    hw = lw // 2

    # Draw the first point
    for i in range(max(0, x1 - hd), min(col, x1 + hd + 1)):
        for j in range(max(0, y1 - hd), min(row, y1 + hd + 1)):
            if (i - x1) ** 2 + (j - y1) ** 2 <= hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Draw the second point
    for i in range(max(0, x2 - hd), min(col, x2 + hd + 1)):
        for j in range(max(0, y2 - hd), min(row, y2 + hd + 1)):
            if (i - x2) ** 2 + (j - y2) ** 2 <= hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Draw the line
    dy = y2 - y1
    dx = x2 - x1
    if abs(dy) <= abs(dx):
        m = dy / dx if dx != 0 else 0
        for x in range(x1, x2 + 1) if x2 > x1 else range(x1, x2 - 1, -1):
            y = round(m * (x - x1) + y1)
            for i in range(max(0, x - hw), min(col, x + hw + 1)):
                for j in range(max(0, y - hw), min(row, y + hw + 1)):
                    Gambar[j, i] = [lr, lg, lb]
    else:
        m = dx / dy if dy != 0 else 0
        for y in range(y1, y2 + 1) if y2 > y1 else range(y1, y2 - 1, -1):
            x = round(m * (y - y1) + x1)
            for i in range(max(0, x - hw), min(col, x + hw + 1)):
                for j in range(max(0, y - hw), min(row, y + hw + 1)):
                    Gambar[j, i] = [lr, lg, lb]

    return Gambar

# Buat gambar untuk setiap garis
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
for titik, parameter in zip(titik_garis, parameter_garis):
    pd, lw, pr, pg, pb, lr, lg, lb = parameter
    Gambar += buat_garis(*titik, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(Gambar)
plt.show()
