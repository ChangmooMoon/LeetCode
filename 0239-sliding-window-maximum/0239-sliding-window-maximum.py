class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        ans = []
        dq = deque()

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])

        for i in range(k, N):
            left = i - k
            if dq and dq[0] == left:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            ans.append(nums[dq[0]])

        return ans
