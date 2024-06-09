class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        for idx, val in enumerate(nums):
            if not st or nums[st[-1]] > val:
                st.append(idx)

        ans = 0
        for i in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]] <= nums[i]:
                ans = max(ans, i-st.pop())
            if not st:
                break

        return ans
        