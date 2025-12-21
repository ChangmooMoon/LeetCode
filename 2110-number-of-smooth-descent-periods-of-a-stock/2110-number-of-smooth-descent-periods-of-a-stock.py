class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)
        
        ans = 0
        i = 0
        while i < N:
            j = i
            while j + 1 < N and prices[j] - prices[j + 1] == 1:
                j += 1
            l = j - i + 1
            ans += l * (l+1) // 2
            i = j + 1
        return ans