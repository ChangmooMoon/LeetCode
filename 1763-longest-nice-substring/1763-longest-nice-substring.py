class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        n = len(s)
        
        def isNice(s) -> bool:
            check = set(s)
            for el in check:
                if el.isupper() and el.lower() not in check:
                    return False
                if el.islower() and el.upper() not in check:
                    return False
    
            return True
        
            
        for i in range(n):
            for j in range(i + 1, n):
                ss = s[i: j + 1]
                if isNice(ss) and len(ans) < len(ss):
                    ans = ss
                    
        return ans
        
"""
1. len(s) = 100
"""