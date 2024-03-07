print("Case 1")
#data bertipe boolean yang dideklarasikan (cara standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=================================================")

#case 2
print("Case 2")
#data bertipe boolean dalam berbagai konteks
#tercatat dengan sendirinya oleh komputer tanpa deklarasi
print(3>2)
print(3+2==5)
print(3<2)
print("=================================================")

#case 3
print("Case 3")
#data bertipe bollean dalam berbagai konteks
#tercatat dengan sendirinya oelh komputer tanpa deklarasi
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus Anda Bayar: Rp ", PajakYangHarusDibayar)

#Part2
#Cae 4
print("Case 4")
#Semua data yang tidak nol (kosong memiliki nilai boolean true
a = 3
b = "Ini data string"
c = ("laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop":"asus", "buku":"buku_teks", "ballpen": "arrow"}
f = { 1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("=================================================")

#part 3
#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai boolean false
a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=================================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai boolean False
class myclass():
    def _len_(self):
        return 0
print(bool(myclass()))
print("=================================================")