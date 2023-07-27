class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        d = [[0] * N for _ in range(N)]
        
        for i in range(N):
            d[0][i] = nums[i]
            
        for i in range(1, N):
            for j in range(0, N - i):
                d[i][j] = (d[i - 1][j] + d[i - 1][j + 1]) % 10
        
        
        return d[N - 1][0]
