# NODE (Pasien)
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


# QUEUE (Linked List)
class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return
        
        removed = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
        
        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama.upper()} (keluhan: {removed.keluhan})")

    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return
        
        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f"  {no}. {current.nama.upper():<10} → {current.keluhan}")
            current = current.next
            no += 1


# SIMULASI SOAL
antrian = Queue()

print("====================================")
print("  SISTEM ANTRIAN POLI UMUM")
print("  RS Sehat Bersama")
print("====================================\n")

# 1
print("[CEK] Apakah antrian kosong? →", "YA, antrian masih kosong." if antrian.is_empty() else "TIDAK")

# 2-4
antrian.enqueue("Nur", "Asam Lambung")
antrian.enqueue("Andre", "Sakit Jantung")
antrian.enqueue("Putra", "Asma")

# 5
print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

# 6
antrian.peek()

# 7
antrian.dequeue()

# 8
antrian.enqueue("Yuli", "Sakit Perut")

# 9
antrian.display()

# 10
antrian.dequeue()

# 11
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

# 12
antrian.clear()

# 13
print("[CEK] Apakah antrian kosong? →", "YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK")

print("\n====================================")
print("  Simulasi Selesai!")
print("======================================")