class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        N = len(high)
        MOD = 10**9 + 7
        low = '0' * (N - len(low)) + low
        
        @cache
        def go(pos, left_cond, right_cond, last_digit, nozero):
            if pos == N:
                return 1
            
            ret = 0
            st = int(low[pos]) if not left_cond else 0
            en = int(high[pos]) + 1 if not right_cond else 10
            
            for next_digit in range(st, en):
                if not nozero or abs(last_digit - next_digit) == 1:
                    ret += go(
                        pos + 1,
                        left_cond or next_digit > int(low[pos]),
                        right_cond or next_digit < int(high[pos]),
                        next_digit,
                        nozero or next_digit != 0
                    )
            return ret % MOD
        
        return go(0, False, False, -1, False)
        
        
    
                    
            
             
'''
1. stepping number 12321, 9878, no leading zero
num 1~10^100
d[i][j] = total nums when i' digit is j

2. 
ex)01~11
0 -> 0~9(except 1): nothing
0 -> 1 : +1
n -> n+1 or n-1: +1

ex)1~9
n -> n+1, or n-1: +1

ex) 100~109 

0 -> 1 -> x
1 -> 0 -> 1
1 -> 2 -> 1,3

'''