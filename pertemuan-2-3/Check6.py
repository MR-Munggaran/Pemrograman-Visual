print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x1 = 100; y1 = 400
x2 = 400; y2 = 100

pd = int(8); pr = 255; pg = 255; pb = 0
lw = int(8); lr = 255; lg = 255; lb = 0

col = int(800)
row = int(800)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i - x1)**2 + (j - y1)**2 < hd**2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if (i - x2)**2 + (j - y2)**2 < hd**2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Calculate the midpoint and third vertex
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    tx = x1 - (y2 - y1) * np.sqrt(3) / 2
    ty = y1 + (x2 - x1) * np.sqrt(3) / 2

    for i in range(int(tx) - hd, int(tx) + hd):
        for j in range(int(ty) - hd, int(ty) + hd):
            if (i - tx)**2 + (j - ty)**2 < hd**2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw lines connecting vertices using a loop
    vertices = [(x1, y1), (int(tx), int(ty)), (x2, y2)]
    for i in range(len(vertices) - 1):
        x_start, y_start = vertices[i]
        x_end, y_end = vertices[i + 1]
        Gambar = draw_line(Gambar, x_start, y_start, x_end, y_end, lw, lr, lg, lb)

    # Connect the last and first vertices
    x_start, y_start = vertices[-1]
    x_end, y_end = vertices[0]
    Gambar = draw_line(Gambar, x_start, y_start, x_end, y_end, lw, lr, lg, lb)

    return Gambar

def draw_line(img, x1, y1, x2, y2, lw, lr, lg, lb):
    hw = int(lw/2)
    dx = x2 - x1
    dy = y2 - y1

    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            x = i
            y = j
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x)**2 + (j - y)**2 < hw**2:
                        img[j, i, 0] = lr
                        img[j, i, 1] = lg
                        img[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x)**2 + (j - y)**2 < hw**2:
                        img[j, i, 0] = lr
                        img[j, i, 1] = lg
                        img[j, i, 2] = lb

    return img

hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
