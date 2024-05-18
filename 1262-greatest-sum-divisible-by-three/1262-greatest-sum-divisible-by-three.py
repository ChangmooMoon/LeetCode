from heapq import heappush, heappop

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        d = [0, float('-inf'), float('-inf')]
        
        for n in nums:
            d_copy = d.copy()
            for rem in range(3):
                d_copy[rem] = max(d[rem], d[(rem - n) % 3] + n)
                
            d = d_copy
            
        return d[0]
        
        '''
        r1 + r2 => r0
        r1 * 3 => r0
        r2 * 3 => r0
        '''
            