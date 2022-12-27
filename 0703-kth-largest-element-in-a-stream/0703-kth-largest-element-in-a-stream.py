class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = nums
        self.k = k
        heapify(self.maxheap)
        
        while len(self.maxheap) > k:
            heapq.heappop(self.maxheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.maxheap, val)
        if len(self.maxheap) > self.k:
            heapq.heappop(self.maxheap)
            
        return self.maxheap[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)