class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = [0 for _ in range(26)]
        
        for ch in s:
            idx = ord(ch) - ord('a')
            v = d[idx]

            for i in range(max(0, idx-k), min(26, idx+k+1)):
                v = max(d[i], v)
            d[idx] = v + 1

        return max(d)
