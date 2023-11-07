class Solution:
    def checkValidString(self, s: str) -> bool:
        left, leftMax = 0, 0
        
        for ch in s:
            if ch == '(':
                left += 1
                leftMax += 1
            elif ch == ')':
                left -= 1
                leftMax -= 1
            elif ch == '*':
                left -= 1
                leftMax += 1
                
            if leftMax < 0:
                return False
            if left < 0: # (*)(
                left = 0
        
        return left == 0
                 
'''
1. * -> open, close, None
- bruteforce : O(3^100)
- greedy: while 0 open
wildcard -> open or else
if open is less than 0, return False
'''