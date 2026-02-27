from tabulate import tabulate
from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

print("=== KONVERTER MATA UANG ===")

# Tampilkan tabel kurs
tabel = []
for kode, nilai in kurs.items():
    tabel.append([kode, f"{nilai:,.0f}".replace(",", ".")])

print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

# Input user
dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

if dari == "IDR" and ke in kurs:
    hasil = idr_ke_mata_uang(jumlah, ke)
    print(f"\n{format_rupiah(jumlah)} = {hasil:.2f} {ke}")

elif ke == "IDR" and dari in kurs:
    hasil = mata_uang_ke_idr(jumlah, dari)
    print(f"\n{jumlah:.2f} {dari} = {format_rupiah(hasil)}")

elif dari in kurs and ke in kurs:
    ke_idr = mata_uang_ke_idr(jumlah, dari)
    hasil = idr_ke_mata_uang(ke_idr, ke)
    print(f"\n{jumlah:.2f} {dari} = {hasil:.2f} {ke}")

else:
    print("Kode mata uang tidak valid!")