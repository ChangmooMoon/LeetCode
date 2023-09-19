class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ret = 0
        
        a = [0] * N # toggle
        flag = 0 # off, on
        
        for i in range(N): 
            if a[i]: # if bit is 1, 
                flag ^= 1
            
            if not nums[i] ^ flag: # if either one is 0
                ret += 1
                flag ^= 1
                
                if i + k < N:
                    a[i + k] = 1
                elif i + k > N:
                    return -1
        return ret
                
        
"""
1. n = 10^5, less than O(N^2) time complexity

"""