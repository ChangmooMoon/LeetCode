class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        l = s + '#' + rev
        
        f = [0] * len(l) # Longest Prefix Suffix
        for i in range(1, len(l)):
            t = f[i - 1]
            
            while t > 0 and l[i] != l[t]:
                t = f[t - 1]
            if l[i] == l[t]:
                t += 1
            f[i] = t
        
        return rev[:len(s) - f[-1]] + s
