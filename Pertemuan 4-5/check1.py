import numpy as np
import matplotlib.pyplot as plt

#besar plot
rowmax = int(1079)
colmax = int(1919)

#coordinat lingkaran
alpha = 520
beta = 904

#besar lingkaran
radius_max = int(300)
batas1 = int(0.5*radius_max)
batas2 = int(0.4*radius_max)
batas3 = int(0.6*radius_max)
batas4 = int(0.8*radius_max)

#gambar lingkaran sesuai rumus (lingkaran 1 < lingkaran 2, lingkaran 2 < lingkaran 3, dst...)
Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)
for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        if ((i - alpha) ** 2 + (j - beta) ** 2) >= 0 and ((i - alpha) ** 2 + (j - beta) ** 2) < batas1 ** 2:
            Gambar[i, j, 2] = 255
        if ((i - alpha) ** 2 + (j - beta) ** 2) >= batas1 ** 2 and ((i - alpha) ** 2 + (j - beta) ** 2) < batas2 ** 2:
            Gambar[i, j, 1] = 255  # hijau
        if ((i - alpha) ** 2 + (j - beta) ** 2) >= batas2 ** 2 and ((i - alpha) ** 2 + (j - beta) ** 2) < batas3 ** 2:
            Gambar[i, j, 2] = 255  # biru
        if ((i - alpha) ** 2 + (j - beta) ** 2) >= batas3 ** 2 and ((i - alpha) ** 2 + (j - beta) ** 2) < batas4 ** 2:
            Gambar[i, j, 1] = 255
            Gambar[i, j, 0] = 255  # kuning
        if ((i - alpha) ** 2 + (j - beta) ** 2) >= batas4 ** 2 and ((i - alpha) ** 2 + (j - beta) ** 2) < radius_max ** 2:
            Gambar[i, j, 0] = 255
            Gambar[i, j, 2] = 255  # magenta

plt.imsave("progvis_lingkaran.jpg", Gambar)
plt.figure()
plt.imshow(Gambar)
plt.show()