class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        s += ' '
        p, q = 0, 0
        for i in range(1, len(s)):
            if s[i] == s[p]:
                q = i
            else:
                if q - p >= 2:
                    ans.append([p, q])
                p = q = i
        return ans
