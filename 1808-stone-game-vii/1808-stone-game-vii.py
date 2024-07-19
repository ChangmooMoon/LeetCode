class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        d = [[-1] * len(stones) for _ in range(len(stones))] #d[i][j]: score diff when pick i, j stone
        
        def solve(i, j, rest):
            if i == j:
                return 0

            if j - i == 1:
                return max(stones[i], stones[j])
            
            if d[i][j] != -1:
                return d[i][j]

            pick_left = rest - stones[i] - solve(i + 1, j, rest - stones[i])
            pick_right = rest - stones[j] - solve(i, j - 1, rest - stones[j])
            d[i][j] = max(pick_left, pick_right)
            return d[i][j]

        return solve(0, len(stones) - 1, sum(stones))