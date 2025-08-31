class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])

        ans = []

        def adj_list(r, c):
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < M and 0 <= nc < N:
                    yield nr, nc
        
        def dfs(r, c):
            if r < 0 or r >= M or c < 0 or c >= N or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            res = 1
            for nr, nc in adj_list(r, c):
                res += dfs(nr, nc)
            return res
        
        is_brick = []
        for r, c in hits:
            is_brick.append(grid[r][c] == 1)
            if grid[r][c] == 1: # erasure
                grid[r][c] = 0 
        
        for c in range(N):
            dfs(0, c)
        
        for i in range(len(hits)-1, -1, -1):
            if not is_brick[i]:
                ans.append(0)
                continue
            
            r, c = hits[i]
            grid[r][c] = 1
            res = 0
            if r == 0:
                res = dfs(r, c)
            else:
                for nr, nc in adj_list(r, c):
                    if grid[nr][nc] == 2:
                        res = dfs(r, c)
                        break
            ans.append(max(0, res - 1))
        
        return ans[::-1]
