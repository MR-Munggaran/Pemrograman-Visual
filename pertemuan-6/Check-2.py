# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
a_lebih_besar_b = a > b

# Cek apakah b lebih besar dari a
b_lebih_besar_a = b > a

# Cek apakah a sama dengan b
a_Sama_dengan_b = a == b

# Hitung PPN a jika lebih dari 10000
if a > 10000:
    ppn_a = a * 0.12
else:
    ppn_a = 0

# Hitung PPN b jika lebih dari 50000
if b > 50000:
    ppn_b = b * 0.12
else:
    ppn_b = 0

# Tambahkan PPN a dan PPN b
total_ppn = ppn_a + ppn_b

del a,b

a_hapus = 'a' not in locals()
b_hapus = 'b' not in locals()

# Print hasil
print("a lebih besar dari b:", a_lebih_besar_b)
print("b lebih besar dari a:", b_lebih_besar_a)
print("a sama dengan b:", a_Sama_dengan_b)
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)
print("Total PPN:", total_ppn)
print("Nilai a sudah dihapus:", a_hapus)
print("Nilai b sudah dihapus:", b_hapus)
