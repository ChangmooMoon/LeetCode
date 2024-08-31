class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        inc, dec = True, True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                inc = False
                break
        
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dec = False
                break

        return inc or dec
                