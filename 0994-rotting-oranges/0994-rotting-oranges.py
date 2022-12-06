class Solution:    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        N, M = len(grid), len(grid[0])
        
        d = [[-1 for i in range(M)] for j in range(N)]
        q = deque([])
        
        f_cnt = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.append((i, j))
                    d[i][j] = 0
                if grid[i][j] == 1:
                    f_cnt += 1
                    
        if f_cnt == 0:
            return 0
                    
        while q:
            r, c = q.popleft()
            for dir in range(4):
                nr, nc = r + dr[dir], c + dc[dir]
                if 0 > nr or 0 > nc or N <= nr or M <= nc:
                    continue
                if d[nr][nc] == -1 and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    d[nr][nc] = d[r][c] + 1
                    
        ret = -1
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    return -1
                ret = max(ret, d[i][j])
        return ret
        
        
        
                    
        
        