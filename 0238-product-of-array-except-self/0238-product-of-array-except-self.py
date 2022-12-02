class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        p = 1
        for i in range(0, len(nums)):
            ret.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= p
            p *= nums[i]
        return ret
            