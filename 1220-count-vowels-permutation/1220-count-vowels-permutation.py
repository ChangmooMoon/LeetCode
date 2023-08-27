class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        d = [[0 for _ in range(n + 1)] for _ in range(5)] # d[i][j] = count of vowels permutation and str[j] is vowel, len is i
        A, E, I, O, U = 0, 1, 2, 3, 4
        
        d[A][1], d[E][1], d[I][1], d[O][1], d[U][1] = 1, 1, 1, 1, 1
        
        for j in range(2, n + 1):
            if d[A][j - 1]:
                d[E][j] += d[A][j - 1] 
            if d[E][j - 1]:
                d[A][j] += d[E][j - 1]
                d[I][j] += d[E][j - 1]
            if d[I][j - 1]:
                d[A][j] += d[I][j - 1] 
                d[E][j] += d[I][j - 1]
                d[O][j] += d[I][j - 1]
                d[U][j] += d[I][j - 1]
            if d[O][j - 1]:
                d[I][j] += d[O][j - 1]
                d[U][j] += d[O][j - 1]
            if d[U][j - 1]:
                d[A][j] += d[U][j - 1] 
        
        ans = 0
        for i in range(5):
            ans += d[i][n]
        
        return ans % MOD
                
"""
1. n 20000,  aeiou -> permutation
2. 
try1 - 5^20000 pruning? no dfs
try2 - dp?

{'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u', 4}

20001 * 5 2d arr, when row == n, meet the conditions
"""