#Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Nilai duplikat akan diabaikan
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True dan 1dianggap memiliki nilai yang sama
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False dan 0dianggap memiliki nilai yang sama
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Untuk menentukan berapa banyak item yang dimiliki suatu set, gunakan len() fungsi tersebut
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Tipe data string, int, dan boolean
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Himpunan yang berisi nilai string, bilangan bulat, dan boolean
set1 = {"abc", 34, True, 40, "male"}

#Apa tipe data dari sebuah himpunan?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Menggunakan konstruktor set() untuk membuat himpunan
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Akses Set Item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Periksa apakah "pisang" ada dalam himpunan tersebut
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Periksa apakah "pisang" TIDAK ada dalam himpunan
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Tambahkan elemen dari tropicalke dalam thisset
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Objek dalam update()metode ini tidak harus berupa himpunan, bisa berupa objek iterasi apa pun (tuple, list, dictionary, dll.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
#Untuk menghapus item dalam satu set, gunakan metode remove(), ataudiscard()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Hapus "pisang" dengan menggunakan discard() metode
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Hapus item secara acak dengan menggunakan pop() metode
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Metode ini clear() mengosongkan himpunan
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#Kata kunci tersebut delakan menghapus seluruh himpunan
thissett = {"apple", "banana", "cherry"}
del thissett


#Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Digunakan |untuk menggabungkan dua himpunan
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Gabungkan beberapa himpunan dengan union()metode
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Digunakan |untuk menggabungkan dua himpunan
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Gabungkan himpunan dengan tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Metode ini update()memasukkan item-item dalam set2 ke dalam set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Metode ini intersection()akan mengembalikan himpunan baru yang hanya berisi item-item yang ada di kedua himpunan tersebut.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Digunakan &untuk menggabungkan dua himpunan
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#ertahankan item yang ada di set1, dan set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#Gabungkan himpunan yang berisi nilai True, False, 1, dan 0, lalu lihat apa yang dianggap sebagai duplikat
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#Metode ini akan mengembalikan himpunan baru yang hanya berisi item dari himpunan pertama yang tidak ada di himpunan lainnya.difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Digunakan -untuk menggabungkan dua himpunan
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#Gunakan difference_update()metode ini untuk hanya menyimpan item dari himpunan pertama yang tidak ada di himpunan lainnya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#Metode ini symmetric_difference()hanya akan menyimpan elemen yang TIDAK ada di kedua himpunan
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#Digunakan ^untuk menggabungkan dua himpunan:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#Gunakan symmetric_difference_update()metode ini untuk mempertahankan item yang tidak ada di kedua set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Python frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

