# =========================
# 1. LIST
# =========================
print("=== LIST ===")
data_list = [1, 2, 3]
data_list.append(4)        # tambah data
data_list.insert(1, 10)    # sisipkan data
data_list.remove(2)        # hapus data

for i in data_list:
    print(i)


# =========================
# 2. TUPLE
# =========================
print("\n=== TUPLE ===")
data_tuple = (1, 2, 3)

for i in data_tuple:
    print(i)


# =========================
# 3. SET
# =========================
print("\n=== SET ===")
data_set = {1, 2, 2, 3}
data_set.add(4)
data_set.remove(1)

print(data_set)


# =========================
# 4. DICTIONARY
# =========================
print("\n=== DICTIONARY ===")
data_dict = {"nama": "Ayu", "umur": 20}
data_dict["alamat"] = "Riau"

for key in data_dict:
    print(key, ":", data_dict[key])


# =========================
# 5. OOP
# =========================
print("\n=== OOP ===")
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampil(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)

mhs1 = Mahasiswa("Ayu", 20)
mhs1.tampil()


# =========================
# 6. LINKED LIST
# =========================
print("\n=== LINKED LIST ===")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# buat node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# sambungkan node
node1.next = node2
node2.next = node3

# traversal (menelusuri)
current = node1
while current:
    print(current.data)
    current = current.next