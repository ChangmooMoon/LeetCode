class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1] + [0] * (N - 1)

        for i in range(1, N):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        rval = 1
        for i in reversed(range(N)):
            ans[i] *= rval
            rval *= nums[i]
        
        return ans
        