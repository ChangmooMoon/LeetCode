class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b, = 0, 0
        for ch in s:
            if ch == 'a':
                a = min(a + 1, b)
            else:
                b += 1
        
        return a

"""
aaba bbab
0011 2223 b
0011 1122 remove a or b

bbaa aaabb
1222 22233 b
0012 22222 remove a or b
"""