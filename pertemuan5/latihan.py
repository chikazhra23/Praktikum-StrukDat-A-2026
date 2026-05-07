stok_barang = [15, 40, 30, 10, 25]
stok_barang[3] = 50
stok_barang.append(5)
stok_barang.sort(reverse=True)
stok_barang = sum(stok_barang)


nilai = [10,25,30,15,40]
rata_rata = sum(nilai)/len(nilai)
print("Stok Aman" if rata_rata > 20 else "Waspada")
print(stok_barang)