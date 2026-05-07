class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
    
        self.root.right.right = Node("F")

    def travers_preorder(self, node):
        hasil = []

        if node:
            hasil.append(node.data)
            hasil += self.travers_preorder(node.left)
            hasil += self.travers_preorder(node.right)

        return hasil
    
    def travers_inorder(self, node):
        hasil = []

        if node:
            hasil += self.travers_inorder(node.left)
            hasil.append(node.data)
            hasil += self.travers_inorder(node.right)

        return hasil
    
    def travers_postorder(self, node):
        hasil = []

        if node:
            hasil += self.travers_postorder(node.left)
            hasil += self.travers_postorder(node.right)
            hasil.append(node.data)

        return hasil
    
    def get_leaf_nodes(self, node, daun):
        if node:
            if node.left is None and node.right is None:
                daun.append(node.data)

            self.get_leaf_nodes(node.left, daun)
            self.get_leaf_nodes(node.right, daun)

tree = BinaryTree()

print('SISTEM AUDIT SIDTRIBUSI "CEPAT SAMPAI"')
print("======================================")

print("[INFO] Membangun Struktur Gudang...")
tree.insert_manual()
print("[INFO] Struktur Berhasil dibuat.\n")

print("HASIL AUDIT:")

preorder = tree.travers_preorder(tree.root)
inorder = tree.travers_inorder(tree.root)
postorder = tree.travers_postorder(tree.root)

print("1. PreOrder :","-".join(preorder))
print("1. In Order :","-".join(inorder))
print("1. Post Order :","-".join(postorder))

leaf = []
tree.get_leaf_nodes(tree.root, leaf)

print("\n[DATA] Gudang Ujung (Leaf Nodes):",",".join(leaf))

print("======================================")
print("Audit Selesai")
