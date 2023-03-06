class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checked = [False] * 10001
        for num in nums:
            checked[num] = True
        
        for i in range(10001):
            if not checked[i]:
                return i