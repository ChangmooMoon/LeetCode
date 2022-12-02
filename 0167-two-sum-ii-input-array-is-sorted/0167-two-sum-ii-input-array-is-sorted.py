class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for i, n in enumerate(numbers):
            if target - n in nums_map:
                return [nums_map[target - n] + 1, i + 1]
            nums_map[n] = i