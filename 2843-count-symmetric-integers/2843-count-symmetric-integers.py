class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n):
            n_str = str(n)
            if len(n_str) % 2 == 1:
                return False
            
            res = 0
            for i in range(0, len(n_str) // 2): # 5 -> 0, 1, 2
                res += int(n_str[i]) - int(n_str[i + len(n_str) // 2])
            return res == 0
                    
        cnt = 0
        for num in range(low, high + 1):
            if isSymmetric(num):
                cnt += 1
        return cnt
                
        
        
"""
1. low high 1~10000, no odd digits 

"""