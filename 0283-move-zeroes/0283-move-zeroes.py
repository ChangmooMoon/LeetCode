class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)

        p = 0
        for i in range(N):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        while p < N:
            nums[p] = 0
            p += 1
