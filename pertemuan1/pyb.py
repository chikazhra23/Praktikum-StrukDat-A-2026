# perbandingan sederhana
print(7 > 5)
print(7 == 10)
print(7 < 5)

# contoh if else
nilai1 = 80
nilai2 = 60

if nilai2 > nilai1:
    print("Nilai kedua lebih besar")
else:
    print("Nilai kedua nggak lebih besar")

# boolean dari isi data
print(bool("Python"))
print(bool(0))

kata = "Ngoding"
angka = 25

print(bool(kata))
print(bool(angka))

# contoh yang bernilai True
bool("belajar")
bool(100)
bool(["pensil", "buku", "pena"])

# contoh yang bernilai False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# contoh class dengan panjang 0
class Contoh:
    def __len__(self):
        return 0

objek = Contoh()
print(bool(objek))

# fungsi yang mengembalikan True
def cekStatus():
    return True

print(cekStatus())

# pakai fungsi di if
def loginBerhasil():
    return True

if loginBerhasil():
    print("Login berhasil!")
else:
    print("Login gagal!")

# cek tipe data
data = 100
print(isinstance(data, int))
