print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x1 = 100; y1 = 400
x2 = 400; y2 = 100

pd = int(8); pr = 255; pg = 255; pb = 0
lw = int(8); lr = 255; lg = 255; lb = 0

col = int(2000)
row = int(2000)

def buat_lingkaran(y, x, r, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)

    for i in range(x - r, x + r):
        for j in range(y - r, y + r):
            if (i - x)**2 + (j - y)**2 < r**2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, :] = pg
                Gambar[j, i, 0] = pb

    # Draw the circle boundary
    for i in range(x - r, x + r):
        for j in range(y - r, y + r):
            if (i - x)**2 + (j - y)**2 < r**2 + hw**2 and (i - x)**2 + (j - y)**2 > r**2 - hw**2:
                Gambar[j, i, 0] = lr
                Gambar[j, i, 1] = lg
                Gambar[j, i, 2] = lb

    return Gambar

hasil = buat_lingkaran((y1 + y2) // 2, (x1 + x2) // 2, int(np.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2), pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
