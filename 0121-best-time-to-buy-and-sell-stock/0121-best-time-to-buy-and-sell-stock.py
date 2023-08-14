class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 1e9, 0
        
        for p in prices:
            L = min(L, p)
            R = max(R, p - L)
            
        return R
"""
1. len 10만, p[i] 1만
"""