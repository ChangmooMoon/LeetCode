class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        length = len(s)

        ans, i = 0, 0
        while i < length:
            if i + 1 < length and roman[s[i]] < roman[s[i + 1]]:
                ans += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                ans += roman[s[i]]
                i += 1
        return ans
