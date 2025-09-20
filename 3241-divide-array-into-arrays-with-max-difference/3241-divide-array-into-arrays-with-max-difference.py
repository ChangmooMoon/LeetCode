class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        if N % 3 != 0: return []
        
        ans = []
        for i in range(0, N, 3):
            a = nums[i:i+3]
            if a[2] - a[0] > k:
                return []
            ans.append(a)
        return ans

"""
2 2 2 2 4 5
[2, 2, 2, 4, 5, 5, 5, 5, 7, 7, 8, 8, 9, 9, 10, 11, 12, 12]
"""