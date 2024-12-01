class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        psum = [0] * (N + 1)
        for i in range(1, N + 1):
            psum[i] = psum[i - 1] + nums[i - 1]

        s = set()
        for i in range(2, N + 1):
            s.add(psum[i - 2] % k)
            if psum[i] % k in s:
                return True
        
        return False
        