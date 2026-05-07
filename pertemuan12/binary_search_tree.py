class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self,id_buku,judul):
        new_node = Node(id_buku,judul)

        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

        print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')

    def insert_node(self, current, new_node):
        if new_node.id_buku < current.id_buku:
            if current.left is None:
                current.left = new_node
            else:
                self.insert_node(current.left, new_node)

        elif new_node.id_buku > current.id_buku:
            if current.right is None:
                current.right = new_node
            else:
                self.insert_node(current.right, new_node)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f'{node.id_buku} - {node.judul}')
            self.inorder(node.right)


    def search(self, node, id_buku):
        if node is None:
            return None

        if id_buku == node.id_buku:
            return node

        elif id_buku < node.id_buku:
            return self.search(node.left, id_buku)

        else:
            return self.search(node.right, id_buku)

  
    def get_min(self):
        current = self.root

        while current.left is not None:
            current = current.left

        return current

   
    def get_max(self):
        current = self.root

        while current.right is not None:
            current = current.right

        return current


    def height(self, node):
        if node is None:
            return -1

        kiri = self.height(node.left)
        kanan = self.height(node.right)

        if kiri > kanan:
            return kiri + 1
        else:
            return kanan + 1

tree = Binary_Search_Tree()

print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")

tree.insert(50, "Dasar Pemrograman")
tree.insert(30, "Struktur Data")
tree.insert(70, "Kecerdasan Buatan")
tree.insert(20, "Matematika Diskrit")
tree.insert(40, "Basis Data")
tree.insert(60, "Jaringan Komputer")
tree.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
tree.inorder(tree.root)

print()

cari1 = tree.search(tree.root, 60)

if cari1:
    print(f'[SEARCH] Mencari ID 60... Ditemukan! Judul: {cari1.judul}')
else:
    print('[SEARCH] Mencari ID 60... Data tidak ditemukan.')


cari2 = tree.search(tree.root, 100)

if cari2:
    print(f'[SEARCH] Mencari ID 100... Ditemukan! Judul: {cari2.judul}')
else:
    print('[SEARCH] Mencari ID 100... Data tidak ditemukan.')

min_buku = tree.get_min()
max_buku = tree.get_max()

print(f'\n[STATISTIK] ID Terkecil: {min_buku.id_buku}')
print(f'[STATISTIK] ID Terbesar: {max_buku.id_buku}')

tinggi = tree.height(tree.root)

print(f'[INFO] Tinggi (Height) Tree: {tinggi}')

print("=========================================")
print("Simulasi Selesaii")

    
