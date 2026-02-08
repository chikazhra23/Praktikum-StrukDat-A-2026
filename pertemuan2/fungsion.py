#Calling a Function
def my_function():
  print("Hello from a function")

my_function()

#fungsi yang sama dapat dipanggil beberapa kali
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#dengan fungsi kode yang sama dapat digunakan lagi
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#fungsi yang mengembalikan nilai
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#nilai kembalian secara langsung:
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#Definisi fungsi tidak boleh kosong. Jika Anda perlu membuat placeholder fungsi tanpa kode apa pun, gunakan pernyataan pass:
def my_function():
  pass

#Python Function Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#parameter
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#Fungsi ini mengharapkan 2 argumen, dan menerima 2 argumen
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Jika fungsi dipanggil tanpa argumen, fungsi tersebut akan menggunakan nilai default
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Nilai default untuk parameter negara
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Anda dapat mengirim argumen dengan sintaks key = value
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Dengan cara ini, pada argumen kata kunci, urutan argumen tidak menjadi masalah.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#Argumen Posisional
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#Mengubah urutan akan mengubah hasilnya
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

#Mencampur Argumen Posisi dan Argumen Kata Kunci
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#Meneruskan Berbagai Tipe Data
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Mengirimkan kamus sebagai argumen
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#Fungsi dapat mengembalikan nilai menggunakan returnpernyataan
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#Mengembalikan Tipe Data yang Berbeda
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Fungsi yang mengembalikan tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Argumen Hanya Berdasarkan Posisi
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#Argumen Khusus Kata Kunci
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#Berdasarkan Posisi Saja dan Pencarian Berdasarkan Kata Kunci Saja
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#Argumen *args dan **kwargs Python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Mengakses argumen individual dari *args
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#Menggunakan *args dengan Argumen Reguler
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#Contoh Praktis dengan *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#Mencari nilai maksimum
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#Gunakan **kwargs** untuk menerima sejumlah argumen kata kunci
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Mengakses nilai dari **kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#Menggunakan **kwargs dengan Argumen Reguler**
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

#Menggabungkan *args dan **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Menggunakan * untuk menguraikan daftar menjadi argumen
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#Menggunakan ** untuk menguraikan kamus menjadi argumen kata kunci
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

#Python Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Variabel lokal dapat diakses dari fungsi di dalam fungsi
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Variabel yang dibuat di luar fungsi bersifat global dan dapat digunakan oleh siapa saja
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#Penamaan Variabel
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Kata Kunci Global
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Untuk mengubah nilai variabel global di dalam sebuah fungsi, rujuk variabel tersebut dengan menggunakan globalkata kunci
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#Kata Kunci Nonlokal
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#Memahami aturan LEGB
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

#Python Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#Menggunakan @changecasedecorator pada dua fungsi
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#Fungsi dengan argumen juga dapat didekorasi
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#Amankan fungsi dengan *args argumen **kwargs
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#Dekorator dengan Argumen
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

#Satu alat dekorasi untuk huruf kapital, dan satu lagi untuk menambahkan ucapan
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

#Biasanya, nama fungsi dapat dikembalikan dengan __name__atribut
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


#Python Lambda
#Tambahkan 10 ke argumen a, dan kembalikan hasilnya
x = lambda a : a + 10
print(x(5))

#Kalikan argumen adengan argumen bdan kembalikan hasilnya
x = lambda a, b : a * b
print(x(5, 6))

#Ringkas argumen a, b, dan clalu kembalikan hasilnya
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Gunakan definisi fungsi tersebut untuk membuat fungsi yang selalu menggandakan angka yang Anda kirimkan
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#gunakan definisi fungsi yang sama untuk membuat fungsi yang selalu melipatgandakan angka yang Anda masukkan menjadi tiga
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#gunakan definisi fungsi yang sama untuk membuat kedua fungsi tersebut, dalam program yang sama
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Lambda dengan Fungsi Bawaan
#Menggunakan Lambda dengan map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Menggunakan Lambda dengan filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Menggunakan Lambda dengan sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Urutkan string berdasarkan panjangnya
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)