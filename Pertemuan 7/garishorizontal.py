import numpy as np
import matplotlib.pyplot as plt

# titik

ya = 200; xa = 100
yb = 200; xb = 1800

# the user decide the point diamter and color
pd = int(8); pr = 255; pg = 0; pb = 255

# the user decide the line widht and color
lw = int(8); lr = 0; lg = 255; lb = 255

# setting the size of the canvas
col = int (2050)
row = int(2040)
print('col, row =', col,'', row)

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


### MAIN PROGRAM
hasil = buat_garis(ya,xa,yb,xb,pd,lw,pr,pg,pb,lr,lg,lb).astype(np.uint8)  # Ubah tipe data menjadi np.uint8


plt.figure()
plt.imshow(hasil)
plt.show()