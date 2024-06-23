class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, sell, cooldown
        t1, t2, t3 = -prices[0], 0, 0
        for p in prices[1:]:
            nt1, nt2, nt3 = t1, t2, t3
            t1 = max(nt1, t3 - p)
            t2 = max(nt2, nt1 + p)
            t3 = max(nt3, nt2)
        
        return t2