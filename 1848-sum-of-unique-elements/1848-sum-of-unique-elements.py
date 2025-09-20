class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(_ for _, v in Counter(nums).items() if v == 1)
        