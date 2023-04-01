class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = format(n, 'b')
        
        prev = bit[0]
        for i in range(1, len(bit)):
            if prev == bit[i]:
                return False
            prev = bit[i]
        return True
            
            
            