class Solution:
    def numTrees(self, n: int) -> int:
        d = [1, 1] + [0] * (n - 1)
        
        for i in range(2, n + 1):
            for j in range(i):
                d[i] += d[j] * d[i - j - 1]
                
        return d[n]