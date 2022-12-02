class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        min_price = 1e9
        
        for price in prices:
            min_price = min(min_price, price)
            ret = max(ret, price - min_price)
            
        return ret
        