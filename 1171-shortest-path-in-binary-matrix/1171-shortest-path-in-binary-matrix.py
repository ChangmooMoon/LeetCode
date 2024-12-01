class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        N = len(grid) # n*n
        if grid[0][0]:
            return -1

        d = [[-1] * N for _ in range(N)]
        d[0][0] = 1
        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and d[nr][nc] == -1):
                    continue
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))
        
        return d[N - 1][N - 1]
