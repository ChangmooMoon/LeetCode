class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = [[False for i in range(N)] for j in range(M)]
        ans = 0
        
        def bfs(r, c) -> int:
            ret = 1
            q = deque([(r, c)])
            visited[r][c] = True
            
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or 0 > nc or M <= nr or N <= nc:
                        continue
                    if grid[nr][nc] != 1 or visited[nr][nc]:
                        continue
                        
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    ret += 1
            return ret        
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, bfs(i, j))
        return ans
                
                
            
                