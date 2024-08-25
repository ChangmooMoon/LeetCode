class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = [[n] for n in nums] # d[i] = subset at i, longest
        ans = []

        for i in reversed(range(len(nums))): # nums[i] < nums[j]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    res = [nums[i]] + d[j]
                    if len(res) > len(d[i]):
                        d[i] = res

            if len(d[i]) > len(ans):
                ans = d[i]
            
        return ans