import numpy as np
import matplotlib.pyplot as plt

# Besar plot
rowmax = 1079
colmax = 1919

# Koordinat titik pusat segi enam
alpha = 520
beta = 904

# Panjang sisi segi enam
sisi = 300

# Titik-titik sudut segi enam
x = []
y = []
for i in range(6):
    sudut_rad = np.pi / 3 * i  # Sudut dalam radian, 60 derajat
    x.append(alpha + sisi * np.cos(sudut_rad))
    y.append(beta + sisi * np.sin(sudut_rad))

# Gambar segi enam
Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)
for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        # Cek apakah titik (i, j) berada dalam segi enam
        if (
            i >= min(x) and i <= max(x) and
            j >= min(y) and j <= max(y) and
            ((i - alpha) ** 2 + (j - beta) ** 2) <= sisi ** 2
        ):
            Gambar[i, j, :] = 255

plt.figure()
plt.imshow(Gambar)
plt.title('Segi Enam')
plt.show()
