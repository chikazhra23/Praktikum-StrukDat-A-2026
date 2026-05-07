class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

  
    def tambahKendaraan(self, plat):
        node_baru = Node(plat)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node_baru

    def hapusKendaraan(self, plat):
        current = self.head
        prev = None

        while current:
            if current.plat == plat:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def tampilkan(self):
        current = self.head
        while current:
            print(current.plat, end=" -> ")
            current = current.next
        print("None")


parkir