class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

        visited = [[False] * N for _ in range(M)]
        ans = []
        r, c, dir = 0, 0, 0
        for _ in range(M * N):
            if not visited[r][c]:
                ans.append(matrix[r][c])
                visited[r][c] = True

            nr, nc = r + dr[dir], c + dc[dir]
            if not (0 <= nr < M and 0 <= nc < N and not visited[nr][nc]):
                dir = (dir + 1) % 4
                
            r, c = r + dr[dir], c + dc[dir]

        return ans
