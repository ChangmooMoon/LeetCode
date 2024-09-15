class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        zero = 0 # 1->0
        one = s.count('1') # 0->1

        ans = one
        for i in range(N-1, -1, -1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            ans = min(ans, zero + one)

        return ans

"""
        0
000000001
"""