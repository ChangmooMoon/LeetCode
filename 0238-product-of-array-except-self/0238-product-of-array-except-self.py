class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        
        n = 1
        for i in range(0, len(nums)):
            ret.append(n)
            n *= nums[i]
        
        n = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= n
            n *= nums[i]
            
        return ret
