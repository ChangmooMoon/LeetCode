class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        a, b, c = Counter(), Counter(), Counter()
        
        for el in nums:
            if a[el - 1]:
                a[el - 1] -= 1
                b[el] += 1
            elif b[el - 1]:
                b[el - 1] -= 1
                c[el] += 1
            elif c[el - 1]:
                c[el - 1] -= 1
                c[el] += 1
            else:   
                a[el] += 1
                
        return a.total() == 0 and b.total() == 0
"""
1. n 10000, less than O(n^2) nlogn, n
"""
            
        
        