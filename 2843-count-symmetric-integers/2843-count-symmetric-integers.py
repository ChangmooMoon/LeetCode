class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n):
            n_str = str(n)
            if len(n_str) % 2 == 1:
                return False
            
            half_sum = 0
            for i in range(0, len(n_str)): # 5 -> 0, 1, 2
                if i < len(n_str) // 2:
                    half_sum += int(n_str[i])
                else:
                    half_sum -= int(n_str[i])
            return half_sum == 0
                    
        cnt = 0
        for num in range(low, high + 1):
            if isSymmetric(num):
                cnt += 1
        return cnt
                
        
        
"""
1. low high 1~10000, no odd digits 

"""