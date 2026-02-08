#Pernyataan if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Memeriksa apakah suatu angka positif
number = 15
if number > 0:
  print("The number is positive")

#Beberapa pernyataan dalam blok if
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Menggunakan variabel boolean
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Menguji berbagai kondisi
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#Pengkategorian kelompok usia
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#Pencari hari dalam seminggu
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#Pernyataan Else Python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Anda juga bisa memiliki elsetanpa tanda elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Memeriksa bilangan genap atau ganjil
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Pengklasifikasi suhu
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Memvalidasi input pengguna
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#Pernyataan satu baris if
a = 5
b = 2
if a > b: print("a is greater than b")

#Satu baris if/ elseyang mencetak sebuah nilai
a = 2
b = 330
print("A") if a > b else print("B")

#cara 3
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Satu baris, tiga hasil
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Mencari nilai maksimum dari dua angka
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#Menetapkan nilai default
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#Operator Logika Python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Periksa apakah a lebih besar dari b, ATAU apakah a lebih besar dari c
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Menggabungkan and, or, dan not
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Gunakan tanda kurung untuk kondisi yang kompleks
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

#Pemeriksaan autentikasi pengguna
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

#Pengecekan rentang dengan operator logika
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

#nested :cara 1
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Memeriksa beberapa kondisi dengan penestingan
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#Tiga tingkatan penestingan
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#Ini adalah pernyataan if bersarang
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#Bisa juga ditulis dengan and
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

#Validasi login dengan pemeriksaan bertingkat
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

#Perhitungan nilai dengan logika bertingkat 
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

#pass_statement :cara 1
a = 33
b = 200

if b > a:
  pass

#empat penampung untuk implementasi di masa mendatang
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#Ini berfungsi dengan benar dengan pass
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#Menggunakan pass di cabang yang berbeda
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#Menggunakan pass dengan fungsi
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet