print("===== Bagian 1 =====")
class StackList:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

#SIMULASI 1
print("=== SIMULASI STACK LIST ===")
browser_list = StackList()

browser_list.push("google.com")
browser_list.push("youtube.com")
browser_list.push("github.com")

print("Halaman saat ini:", browser_list.peek())
print("Jumlah riwayat:", browser_list.size())

print("Back dari:", browser_list.pop())
print("Sekarang di:", browser_list.peek())

print("Back dari:", browser_list.pop())
print("Sekarang di:", browser_list.peek())

print("Back dari:", browser_list.pop())
print("Coba back lagi:", browser_list.pop())


print("===== Bagian 2 =====")
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top is None
    
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Ri3wayat Kosong"
        
        remove_url = self.top.url
        self.top = self.top.next
        self.count += 1
        return remove_url
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url
    
    def size(self):
        return self.count
 #SIMULASI 2
browser_linked = StackLinkedList()

browser_linked.push("google.com")
browser_linked.push("youtube.com")
browser_linked.push("github.com")

print("Halaman saat ini:", browser_linked.peek())
print("Jumlah riwayat:", browser_linked.size())

print("Back dari:", browser_linked.pop())
print("Sekarang di:", browser_linked.peek())

print("Back dari:", browser_linked.pop())
print("Sekarang di:", browser_linked.peek())

print("Back dari:", browser_linked.pop())
print("Coba back lagi:", browser_linked.pop())

