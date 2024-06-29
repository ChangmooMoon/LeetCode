class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""
            for i in range(0, len(s), k):
                digit = 0
                for j in range(i, i + k):
                    if len(s) > j:
                        digit += int(s[j])
                res += str(digit)
            s = res

        return s
