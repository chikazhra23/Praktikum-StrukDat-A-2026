thislist = ["apple", "banana", "cherry"]
print(thislist)

#dapat mempunyai value yang sama
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#untuk menghitung jumlah value
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#dengan tipe data yang berbeda
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#list yang berisi berbagai tipe data
list1 = ["abc", 34, True, 40, "male"]

#untuk mengetahui tipe data
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#untuk membuat sebuah list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist

#
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists
#Cetak semua item dalam daftar, satu per satu
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Cetak semua item dengan merujuk pada nomor indeksnya
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Cetak semua item, menggunakan whileperulangan untuk menelusuri semua nomor indeks
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Sebuah perulangan singkat foryang akan mencetak semua item dalam sebuah daftar
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Dengan list comprehension, Anda dapat melakukan semua itu hanya dengan satu baris kode
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Hanya terima barang yang bukan "apel"
newlist = [x for x in fruits if x != "apple"]

#Tanpa ifpernyataan apa pun
newlist = [x for x in fruits]

#Anda dapat menggunakan range()fungsi tersebut untuk membuat objek yang dapat diiterasi
newlist = [x for x in range(10)]

#Hanya terima angka yang lebih kecil dari 5
newlist = [x for x in range(10) if x < 5]

#Ubah nilai-nilai dalam daftar baru menjadi huruf besar
newlist = [x.upper() for x in fruits]

#Atur semua nilai dalam daftar baru menjadi 'hello'
newlist = ['hello' for x in fruits]

#Kembalikan "jeruk" sebagai ganti "pisang"
newlist = [x if x != "banana" else "orange" for x in fruits]

#Python - Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Urutkan daftar secara numerik
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Urutkan daftar secara menurun
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Urutkan daftar secara menurun
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Urutkan daftar berdasarkan seberapa dekat angka tersebut dengan 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Pengurutan berdasarkan huruf besar dan kecil dapat memberikan hasil yang tidak terduga
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Lakukan pengurutan daftar tanpa memperhatikan huruf besar/kecil
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Metode ini reverse()membalik urutan pengurutan elemen saat ini
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Buat salinan daftar dengan list()metode
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Buat salinan daftar dengan :operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Python - Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Tambahkan list2 ke list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Gunakan extend()metode untuk menambahkan list2 di akhir list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

