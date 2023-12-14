class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m: return False

        s1Map, s2Map = Counter(s1), Counter()
        for i in range(m):
            s2Map[s2[i]] += 1
            if i >= n:
                ch = s2[i - n]
                s2Map[ch] -= 1
                if s2Map[ch] == 0:
                    del s2Map[ch]
            if s1Map == s2Map: return True
    
        return False    

"""
1. s1, s2 len 10000
sliding window
"""