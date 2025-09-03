class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        N = len(nums)
        checker = set()
        for i in range(N-1):
            if nums[i]+nums[i+1] in checker:
                return True
            checker.add(nums[i]+nums[i+1])
        return False
