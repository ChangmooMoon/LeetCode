class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        ans = 0

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    continue
                l = r = 0

                i2, j2 = i - 1, j - 1
                while i2 >= 0 and j2 >= 0 and s[i2] == t[j2]:
                    l += 1
                    i2 -= 1
                    j2 -= 1

                i2, j2 = i + 1, j + 1
                while i2 < n and j2 < m and s[i2] == t[j2]:
                    r += 1
                    i2 += 1
                    j2 += 1

                ans += (l + 1) * (r + 1)

        return ans
