class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            if target - val in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - val) + i + 1]
