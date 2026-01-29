# contoh string pakai petik
print("Halo")
print('Hai')

print("Struktur Data")
print("Matakuliah 2'")
print('Matakuliah 2"')

# simpan string ke variabel
kata = "Belajar Python"
print(kata)

# string panjang (multi baris)
kata = """Ini contoh teks panjang,
dipakai kalau catatannya
lebih dari satu baris
biar rapi."""
print(kata)

kata = '''Ini juga contoh teks panjang,
isinya bisa 
beberapa baris.'''
print(kata)

# slicing string
teks = "Ngoding Python!"
print(teks[3:8])

teks = "Ngoding Python!"
print(teks[:7])

teks = "Ngoding Python!"
print(teks[3:])

teks = "Ngoding Python!"
print(teks[-7:-1])

# mengubah string
kalimat = "Belajar Python itu Seru"
print(kalimat.upper())

kalimat = "Belajar Python itu Seru"
print(kalimat.lower())

kalimat = "   Santai tapi fokus   "
print(kalimat.strip())

kalimat = "Belajar Python itu Seru"
print(kalimat.replace("Seru", "Asik"))

kalimat = "Ngoding, itu, asik"
print(kalimat.split(","))

# menggabungkan string
kata1 = "Ngoding"
kata2 = "Seru"
hasil = kata1 + kata2
print(hasil)

kata1 = "Ngoding"
kata2 = "Seru"
hasil = kata1 + " " + kata2
print(hasil)

# format string
umur = 17
teks = f"Umur sekarang {umur} tahun"
print(teks)

harga = 12500
teks = f"Harganya {harga} rupiah"
print(teks)

harga = 12500
teks = f"Harganya {harga:.2f} rupiah"
print(teks)

teks = f"Total bayar {3 * 12500} rupiah"
print(teks)

# escape character
teks = "Katanya dia \"semangat\" hari ini"
print(teks)
