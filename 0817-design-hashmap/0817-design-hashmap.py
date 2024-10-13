class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    
    def __init__(self):
        self.size = 1024
        self.table = [None] * self.size

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return

        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next


    def get(self, key: int) -> int:
        idx = key % self.size
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        curr = self.table[idx]
        if not curr:
            return
        if curr.key == key:
            self.table[idx] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)