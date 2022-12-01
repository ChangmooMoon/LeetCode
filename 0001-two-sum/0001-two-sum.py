class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, n in enumerate(nums):
            nums_map[n] = idx
        
        for idx, n in enumerate(nums):
            if target - n in nums_map and idx != nums_map[target - n]:
                return [idx, nums_map[target - n]]