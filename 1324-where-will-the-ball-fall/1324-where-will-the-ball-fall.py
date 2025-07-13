class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        ans = []

        for j in range(N):
            curr_j = j
            for i in range(M):
                dir = grid[i][curr_j]
                next_j = curr_j + dir
                if next_j < 0 or next_j >= N or grid[i][next_j] != dir:
                    curr_j = -1
                    break

                curr_j = next_j
            ans.append(curr_j)
        
        return ans
        