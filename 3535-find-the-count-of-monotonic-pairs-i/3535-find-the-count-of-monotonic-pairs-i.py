class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = int(1e9) + 7
        n, m = len(nums), max(nums)
        d = [[0] * (m + 1) for _ in range(n)]

        for i in range(nums[0] + 1): # start
            d[0][i] = 1
        for i in range(1, n):
            psum = [d[i-1][0]] + [0] * m
            for j in range(1, m + 1):
                psum[j] = (psum[j - 1] + d[i - 1][j]) % MOD

            for j in range(nums[i] + 1):
                k = min(j, j + nums[i - 1] - nums[i])
                if k >= 0:
                    d[i][j] = psum[k] % MOD
        
        ans = 0
        for i in range(nums[-1] + 1):
            ans = (ans + d[-1][i]) % MOD

        return ans
