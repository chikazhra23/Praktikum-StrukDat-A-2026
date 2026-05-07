# =========================================
# UTS PRAKTIKUM STRUKTUR DATA
# Studi Kasus: Sistem Antrian Peminjaman Perpustakaan
# =========================================

# -----------------------------------------
# DATA AWAL
# -----------------------------------------
pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False},
]

# =========================================
# SOAL 1 - LIST DAN DICTIONARY
# =========================================

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")

    for i, p in enumerate(pengunjung_hari_ini, start=1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i:<2} | {p['id']:<4} | {p['nama']:<6} | {p['usia']:<4} | {p['kategori']:<8} | {status}")

def filter_belum_kembali():
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, start=1):
        print(f"{i}. {nama}")

    print(f"Total belum kembali: {len(belum)} pengunjung")


# =========================================
# SOAL 2 - TUPLE DAN SET
# =========================================

def info_perpustakaan():
    info = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )

    print("\nInfo Perpustakaan:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

def rekap_kategori():
    kategori_unik = set(p["kategori"] for p in pengunjung_hari_ini)

    print("\nKategori Buku Unik:", kategori_unik)
    print("Jumlah kategori:", len(kategori_unik))

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


# =========================================
# SOAL 3 - OOP
# =========================================

class Pengunjung:
    total = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total += 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print("\nID       :", self.__id)
        print("Nama     :", self.__nama)
        print("Kategori :", self.__kategori)

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.total


class PengunjungPrioritas(Pengunjung):
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


# =========================================
# SOAL 4 - SINGLE LINKED LIST
# =========================================

class Node:
    def __init__(self, data):
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
            print("Antrian kosong")
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

    def cari(self, nama):
        print(f"\nMencari '{nama}'...")
        current = self.head
        posisi = 1

        while current:
            if current.data["nama"] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['kategori']} (posisi ke-{posisi})")
                return
            current = current.next
            posisi += 1

        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        print(f"\nMenghapus pengunjung dengan ID {id}...")

        if self.head is None:
            print("Antrian kosong")
            return

        if self.head.data["id"] == id:
            print(f"{self.head.data['nama']} ({id}) berhasil dihapus dari antrian.")
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data["id"] == id:
                print(f"{current.next.data['nama']} ({id}) berhasil dihapus dari antrian.")
                current.next = current.next.next
                return
            current = current.next

        print("ID tidak ditemukan")

    def hitung(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# =========================================
# PEMANGGILAN PROGRAM
# =========================================

# Soal 1
tampilkan_pengunjung()
filter_belum_kembali()

# Soal 2
info_perpustakaan()
rekap_kategori()

# Soal 3
p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
p2.tampilkan_info()

print("\nTotal pengunjung terdaftar:", Pengunjung.hitung_pengunjung())

# Soal 4
antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})

antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())