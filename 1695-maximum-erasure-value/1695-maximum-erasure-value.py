class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
            ans, curr = 0, 0
            seen = set()

            l = 0
            for r, num in enumerate(nums):
                  while num in seen:
                        curr -= nums[l]
                        seen.remove(nums[l])
                        l += 1
                  seen.add(nums[r])
                  curr += nums[r]
                  ans = max(ans, curr)

            return ans