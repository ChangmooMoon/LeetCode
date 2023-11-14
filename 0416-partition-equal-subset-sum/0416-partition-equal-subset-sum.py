class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        
        d = [[1] * (n + 1) for _ in range(target + 1)]
        for i in range(1, target + 1):
            d[i][0] = 0
        
        for i in range(1, target + 1):
            for j in range(1, n + 1):
                d[i][j] = d[i][j - 1]
                
                if i >= nums[j - 1]:
                    d[i][j] |= d[i - nums[j - 1]][j - 1]
                    
        return d[target][n]
    
"""
1. 2 partition, N 200, el 1~100
2. quick sort partitioning? dp?
n 200, sum(nums) 200 * 100

d[i][j] = subset {0~j-1}' sum is equal to I ? 1:0
"""