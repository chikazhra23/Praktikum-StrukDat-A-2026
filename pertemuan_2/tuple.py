#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple memperbolehkan nilai duplikat
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Cetak item terakhir dari tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Kembalikan item ketiga, keempat, dan kelima
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Contoh ini mengembalikan item dari awal hingga, tetapi TIDAK termasuk, "kiwi"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#Contoh ini mengembalikan item dari "cherry" hingga akhir
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Contoh ini mengembalikan item dari indeks -4 (termasuk) hingga indeks -1 (tidak termasuk)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Periksa apakah "apel" ada dalam tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Ubah tuple menjadi list, tambahkan "orange", lalu ubah kembali menjadi tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Buat tuple baru dengan nilai "orange", lalu tambahkan tuple tersebut
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Ubah tuple menjadi daftar, hapus "apple", dan ubah kembali menjadi tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Kata kunci tersebut deldapat menghapus tuple sepenuhnya
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Tetapkan nilai-nilai lainnya sebagai daftar bernama "merah"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Tambahkan daftar nilai ke variabel "tropic"
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Gunakan fungsi ` range()and` len()untuk membuat objek iterable yang sesuai
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Cetak semua item, menggunakan whileperulangan untuk menelusuri semua nomor indeks
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Jika Anda ingin mengalikan isi tuple sejumlah kali tertentu, Anda dapat menggunakan * operator
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


