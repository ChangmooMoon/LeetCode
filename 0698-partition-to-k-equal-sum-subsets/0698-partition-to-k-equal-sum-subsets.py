class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        target_sum = sum(nums) // k
        subsets = [0] * k
        nums.sort(reverse=True)
        
        def bt(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= target_sum:
                    subsets[j] += nums[i]
                    if bt(i + 1):
                        return True
                    subsets[j] -= nums[i]
                    
                    if subsets[j] == 0:
                        break
            return False
    
        return bt(0)
