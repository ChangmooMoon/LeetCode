class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bit = 0
        for i in range(len(s) - k + 1):
            bit |= 1 << int(s[i:i+k], 2) # flip 0 -> 1 in range
        
        return bit == (1 << 2**k) - 1
            
    