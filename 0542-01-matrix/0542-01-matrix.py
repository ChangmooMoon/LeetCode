class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        d = [[-1 for _ in range(m)] for _ in range(n)]
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    d[i][j] = 0
                    
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and d[nr][nc] == -1:
                    d[nr][nc] = d[r][c] + 1
                    q.append((nr, nc))
        
        return d
                
        
                    
                
        