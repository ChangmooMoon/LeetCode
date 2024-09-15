class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
        N, M = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            ret = grid[r][c]
            grid[r][c] = 0

            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc]:
                    ret += dfs(nr, nc)

            return ret
            

        for r in range(N):
            for c in range(M):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))
        return ans
        