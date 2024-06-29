class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""
            for i in range(0, len(s), k):
                digit = 0
                for d in s[i:i+k]:
                    digit += int(d)
                res += str(digit)
            s = res

        return s
