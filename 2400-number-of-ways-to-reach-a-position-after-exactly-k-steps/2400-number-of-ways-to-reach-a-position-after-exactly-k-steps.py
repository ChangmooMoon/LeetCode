class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        restStep = k - abs(endPos - startPos)
        if restStep < 0 or restStep & 1:
            return 0
        
        left, right = restStep // 2, k - restStep // 2
        return self.nCk(left + right, min(left, right))
    
    def nCk(self, n, k):
        MOD = 10**9 + 7
        d = [0] * (k + 1)
        d[0] = 1
        
        for _ in range(n):
            for j in range(k, 0, -1):
                d[j] = (d[j] + d[j - 1]) % MOD
        
        return d[k]
        
"""
1. st -> en, k step, 1 <= st, en, k <= 1000
2. dp? O(1000^2)

right = (k + en - st) // 2
left = k - right
"""
        