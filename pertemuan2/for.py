#for_loops :cara 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Melakukan perulangan melalui sebuah string
for x in "banana":
  print(x)

#Pernyataan jeda (break)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Keluar dari perulangan ketika xnilainya "pisang", tetapi kali ini perintah break diletakkan sebelum perintah print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Pernyataan lanjutan (continue)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Fungsi range()
for x in range(6):
  print(x)

#Menggunakan parameter awal
for x in range(2, 6):
  print(x)

#ambahkan angka 3 pada urutan tersebut (nilai default adalah 1)
for x in range(2, 30, 3):
  print(x)

#Hentikan perulangan saat xnilainya 3, dan lihat apa yang terjadi dengan elseblok tersebut
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Perulangan Bersarang
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Tuliskan setiap kata sifat untuk setiap buah
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Pernyataan pass
for x in [0, 1, 2]:
  pass