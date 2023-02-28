class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num);
        
        for i in range(1, k + 1):
            num = heapq.heappop(q)
            if i == k:
                return -num
        
        