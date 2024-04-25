# Inisialisasi set buah
buah = {"apel", "jeruk", "pisang"}



print("Kerangjang buah 1 :", buah)
print('='*200)


buah.add("anggur")
print("Ibu membeli buah anggur maka dikeranjang ada buah :", buah)
print('='*200)


buah.update(["mangga", "nanas"])
print("Ibu membeli lagi mangga dan nanas maka dikeranjang ada buah:", buah)
print('='*200)


buah.remove("pisang")
print("Ibu tidak jadi membeli pisang, maka di keranjang ada:", buah)
print('='*200)


Buah_pop = buah.pop()
print("kemudian ibu tidak membeli buah pertama kali yang dimasukan ke keranjang yaitu :", Buah_pop)
print("maka di keranjang ada:", buah)
print('='*200)


Keranjang2 = {"apel", "durian", "semangka"}
buah_gabungan = buah.union(Keranjang2)
print("ibu mengambil keranjang lain untuk membeli buah :", Keranjang2)
print("Jika digabungkan maka buahnya ada :", buah_gabungan)
print('='*200)