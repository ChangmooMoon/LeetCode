class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.heap = [] # heap
        self.set = set()

    def popSmallest(self) -> int:
        if not self.heap:
            target = self.num
            self.num += 1
        else:
            target = heappop(self.heap)
            self.set.remove(target)

        return target
            
    def addBack(self, num: int) -> None:
        if self.num <= num or num in self.set:
            return
        heappush(self.heap, num)
        self.set.add(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
