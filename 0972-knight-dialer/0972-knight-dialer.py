class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = int(1e9) + 7
        dr = [-2, -1, 1, 2, 2, 1, -1, -2]
        dc = [1, 2, 2, 1, -1, -2, -2, -1]

        d = [[1] * 3 for _ in range(4)]
        d[3][0] = 0  # *
        d[3][2] = 0  # #

        for _ in range(n - 1):
            next_d = [[0] * 3 for _ in range(4)]
            for r in range(4):
                for c in range(3):
                    if r == 3 and (c == 0 or c == 2):
                        continue
                    for i in range(8):
                        nr, nc = r + dr[i], c + dc[i]
                        if nr == 3 and (nc == 0 or nc == 2):
                            continue
                        if 0 <= nr < 4 and 0 <= nc < 3:
                            next_d[nr][nc] = (next_d[nr][nc] + d[r][c]) % MOD
            d = next_d

        ans = 0
        for i in range(4):
            for j in range(3):
                ans = (ans + d[i][j]) % MOD

        return ans
