class MyHashSet:

    def __init__(self):
        self.capa = 1024
        self.bucket = [[] for _ in range(self.capa)]
        
    def add(self, key: int) -> None:
        hkey = key % self.capa
        if not self.contains(key):
            self.bucket[hkey].append(key)
        
    def remove(self, key: int) -> None:
        hkey = key % self.capa
        if self.contains(key):
            self.bucket[hkey].remove(key)

    def contains(self, key: int) -> bool:
        hkey = key % self.capa
        return key in self.bucket[hkey]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)