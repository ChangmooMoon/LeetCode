class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        heapify(nums)
        for _ in range(k):
            n = heappop(nums)
            heappush(nums, n + 1)
        
        ans = 1
        for el in nums:
            ans = (ans * el) % MOD
        return ans
            
            
"""
1. increase k times by 1
n, k 10^5
"""