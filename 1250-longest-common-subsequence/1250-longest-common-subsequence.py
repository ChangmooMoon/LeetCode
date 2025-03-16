class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        d = [[0]*(N+1) for _ in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                if text1[i-1] == text2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        
        return d[M][N]

"""
d(i,j) = max d(i-1,j), d(i,j-1)
"""