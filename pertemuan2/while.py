#while loops :cara 1
#Cetak i selama i kurang dari 6
i = 1
while i < 6:
  print(i)
  i += 1

#Pernyataan jeda
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Pernyataan lanjutan
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Cetak pesan setelah kondisinya salah
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")