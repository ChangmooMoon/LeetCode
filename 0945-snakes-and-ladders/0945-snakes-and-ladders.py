class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        visited = [[0] * N for _ in range(N)]

        def curr_pos(num) -> tuple:
            r, c = divmod(num - 1, N) # 1 -> 5 0, 7->4 5
            rr = N - 1 - r
            cc = c if r % 2 == 0 else N - 1 - c
            return rr, cc
        
        q = deque([(1, 0)])
        sr, sc = curr_pos(1)
        visited[sr][sc] = 1
        while q:
            curr, roll = q.popleft()
            if curr == N * N:
                return roll
            
            for i in range(1, 7):
                if curr + i > N * N:
                    break

                nr, nc = curr_pos(curr + i)
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                if board[nr][nc] != -1:
                    q.append((board[nr][nc], roll + 1))
                else:
                    q.append((curr + i, roll + 1))
        return -1