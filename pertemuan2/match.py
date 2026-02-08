#Contoh di bawah ini menggunakan nomor hari dalam seminggu untuk mencetak nama hari dalam seminggu
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#Gunakan karakter garis bawah _ sebagai nilai kasus terakhir jika Anda ingin blok kode dieksekusi ketika tidak ada kecocokan lain
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

#Gunakan karakter pipa | sebagai operator "atau" dalam evaluasi kasus untuk memeriksa kecocokan lebih dari satu nilai dalam satu kasus
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

#Anda dapat menambahkan ifpernyataan dalam evaluasi kasus sebagai pengecekan kondisi tambahan
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")