class Solution:
    def sumScores(self, s: str) -> int:
        N = len(s)
        
        z = [0] * N
        l, r = 0, 0  # init p, score
        ans = 0

        for i in range(1, N):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])       

            while i + z[i] < N and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
            ans += z[i]
        
        return ans + N

'''
babab
b       1
ab      0
bab     3
abab    0
babab   5


'''
