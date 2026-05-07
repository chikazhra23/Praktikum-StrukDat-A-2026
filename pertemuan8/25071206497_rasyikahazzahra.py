pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi","kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains","kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi","kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum","kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains","kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum","kembali": False},
]

 
 #SOAL 1
def tampilkan_penggunjung():
    print("===== DATA PENGUNJJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")

    for i, p in enumerate (pengunjung_hari_ini, start=1):
        status = "Sudah Kembali" if p ['kembali'] else "Belum Kembali"
        print (f"{i:<2} | {p['id']:<4} | {p['nama']:<6} | {p['usia']:<4} | {p['kategori']:<8} | {status}")

tampilkan_penggunjung()

def filter_belum_kembali():
    belum=[p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort

    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, start=1): 
        print (f"{i} .{nama}")

    print(f"Total belum kembali: {len(belum)} pengunjung")

filter_belum_kembali()

#SOAL 2

def info_perpustakaan():
    info =(
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )

    print("\nInfo Perpustakaan:")
    print("Nama     :",info[0])
    print("Alamat   :",info[1])
    print("Telp     :",info[2])

info_perpustakaan()

def rekap_kategori():
    kategori_unik = set(p["kategori"] for p in pengunjung_hari_ini)

    print("\nKategori Unik :", kategori_unik)
    print("Jumlah Kategori :", len(kategori_unik))

    hitung = {}
    for p in pengunjung_hari_ini:
        kategori = p["kategori"]
        if kategori in hitung:
            hitung[kategori] += 1
        else:
            hitung[kategori] = 1

    print("\nRekap per kategori:")

    for k, v in hitung.items():
        print(f"{k} : {v} pengunjung")

    maksimum = max(hitung.values())
    terbanyak = [k for k, v in hitung.items() if v == maksimum]

    print("\nKategori terbanyak:", ", ".join(terbanyak), f"({maksimum} pengunjung)")

rekap_kategori()

#SOAL3
class pengunjung:
    total = 0

    def __init__(self, id, nama, kategori):
        self.__id= id
        self.__nama= nama
        self.__kategori= kategori
        pengunjung.total +=1
    
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):

        print("\nID     :", self.__id)
        print("NAMA   :", self.__nama)
        print("KATEGORI     :", self.__kategori)


    def hitung_pengunjung():
        return pengunjung.total


class PengunjungPrioritas(pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        print("\nID         :", self.get_id())
        print("Nama       :", self.get_nama())
        print("Kategori   :", self.get_kategori())
        print("Prioritas  :", self.prioritas)

        if self.prioritas == "Mendesak":
            print("** Layani segera! **")

p1 = pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
p2.tampilkan_info()

print("\nTotal pengunjung terdaftar:", pengunjung.hitung_pengunjung())



#SOAL 4
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")

        if self.head is None:
            print("Antrian Kosong")
            return

        current = self.head
        no = 1

        while current:
            d = current.data
            print(f"[{no}] {d['id']} - {d['nama']} | {d['kategori']}")
            current = current.next
            no += 1

        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self):
        if self.head is None:
            print("Antrian kosong")
            return

        print("\nMemanggil pengunjung berikutnya...")
        data = self.head.data
        print(f"Silakan masuk: {data['nama']} ({data['id']}) - {data['kategori']}")
        self.head = self.head.next

    def cari(nama):
        pass

    def hapus_berdasarkan_id(id):
        pass

    def hitung():
        pass

