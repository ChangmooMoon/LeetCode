class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0] * n for _ in range(m)]
        for i in range(n):
            d[0][i] = 1
        for i in range(m):
            d[i][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i - 1][j] + d[i][j - 1]
        
        return d[m - 1][n - 1]
        
"""
1. [0][0] -> [m - 1][n - 1]
"""