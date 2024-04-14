class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)

        cnt = 0
        for i in range(N):
            for j in range(N):
                curr = grid[i][j]
                row = grid[i]
                col = [grid[r][j] for r in range(N)]
                grid[i][j] = min(max(row), max(col))
                cnt += grid[i][j] - curr
            
        return cnt
