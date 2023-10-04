class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        s = set(arr)
        ans = 0
        
        for i in range(N):
            for j in range(i + 1, N):
                p1, p2 = arr[i], arr[j]
                ret = 1
                
                while p2 in s:
                    p1, p2 = p2, p1 + p2
                    ret += 1
                
                if ret >= 3:
                    ans = max(ans, ret)
                    
        return ans            
"""
1. n 1000 
n^2 = 1m
"""