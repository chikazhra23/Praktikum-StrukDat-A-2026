#Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Cetak nilai "merek" dari kamus tersebut
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Nilai duplikat akan menimpa nilai yang sudah ada
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Tipe data string, int, boolean, dan list
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Cetak tipe data dari sebuah kamus
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Menggunakan metode dict() untuk membuat kamus:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Access Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Get the value of the "model" key:
x = thisdict.get("model")

#Get a list of the keys:
x = thisdict.keys()

#Tambahkan item baru ke kamus asli, dan lihat bahwa daftar kunci juga ikut diperbarui
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#Dapatkan daftar nilainya:
x = thisdict.values()

#Lakukan perubahan pada kamus asli, dan lihat bahwa daftar nilai juga ikut diperbarui
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Tambahkan item baru ke kamus asli, dan lihat bahwa daftar nilai juga ikut diperbarui
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Dapatkan daftar pasangan kunci:nilai.
x = thisdict.items()

#Lakukan perubahan pada kamus asli, dan lihat bahwa daftar item juga ikut diperbarui
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Tambahkan item baru ke kamus asli, dan lihat bahwa daftar item juga ikut diperbarui
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Periksa apakah "model" ada dalam kamus
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Perbarui "tahun" mobil dengan menggunakan update() metode berikut
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Add Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Tambahkan item warna ke kamus dengan menggunakan update() metode
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Remove Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Metode ini popitem()menghapus item terakhir yang dimasukkan (pada versi sebelum 3.7, item acak yang dihapus)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Kata kunci tersebut delmenghapus item dengan nama kunci yang ditentukan
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Metode ini clear()mengosongkan kamus
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop Dictionaries
for x in thisdict:
  print(x)

#Cetak semua nilai dalam kamus, satu per satu:
for x in thisdict:
  print(thisdict[x])

#Anda juga dapat menggunakan values()metode ini untuk mengembalikan nilai-nilai dari sebuah kamus:
for x in thisdict.values():
  print(x)

#Lakukan perulangan melalui kunci dan nilai , dengan menggunakan items()metode:
for x, y in thisdict.items():
  print(x, y)

#Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Buat salinan kamus dengan dict() fungsi:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Buat tiga kamus, lalu buat satu kamus yang akan berisi ketiga kamus lainnya
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Tuliskan nama anak ke-2:
print(myfamily["child2"]["name"])

#Lakukan perulangan melalui kunci dan nilai dari semua kamus bersarang
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])