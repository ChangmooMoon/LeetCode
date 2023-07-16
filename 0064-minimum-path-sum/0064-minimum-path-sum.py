class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        global n, m, a, memo
        n, m = len(grid), len(grid[0])
        a = grid
        memo = {}
        
        return self.go(0, 0)
    
    def go(self, r, c) -> int:
        if r >= n or c >= m:
            return float('inf')
        if (r, c) in memo:
            return memo[(r, c)]
        if r == n - 1 and c == m - 1:
            return a[r][c]
        
        memo[(r, c)] = min(self.go(r + 1, c), self.go(r, c + 1)) + a[r][c]
        return memo[(r, c)]
        