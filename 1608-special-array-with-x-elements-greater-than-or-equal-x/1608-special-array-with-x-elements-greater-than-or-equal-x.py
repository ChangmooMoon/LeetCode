class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            cnt = 0
            for el in nums:
                if el >= i:
                    cnt += 1
            if cnt == i:
                return cnt
        return -1
            
"""
1. n 100
"""