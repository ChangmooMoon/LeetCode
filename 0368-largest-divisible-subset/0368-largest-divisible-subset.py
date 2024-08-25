class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = [[n] for n in nums] # d[i] = subset at i, longest
        ans = []

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    res = [nums[i]] + d[j]
                    d[i] = res if len(res) > len(d[i]) else d[i]
            ans = d[i] if len(d[i]) > len(ans) else ans
            
        return ans