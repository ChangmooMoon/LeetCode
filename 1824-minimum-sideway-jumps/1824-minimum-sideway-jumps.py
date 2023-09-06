class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = float("inf")
        n = len(obstacles)
        d = [[INF] * 3 for _ in range(n)]
        
        d[0][1] = 0
        d[0][0] = d[0][2] = 1
        
        for i in range(1, n):
            for j in range(3):
                if obstacles[i - 1] == j + 1 or obstacles[i] == j + 1: # way prev was rock
                    d[i][j] = INF
                else: # possible block
                    col1, col2 = (j + 1) % 3, (j + 2) % 3
                    d[i][j] = min(d[i - 1][j], d[i - 1][col1] + 1, d[i - 1][col2] + 1)
                    
        return min(d[n - 1])
                

"""
1. 3 * (n + 1) grid, starts at (1, 0)
"""