class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(2, n + 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
            
        return (a + e + i + o + u) % MOD
                
"""
1. n 20000,  aeiou -> permutation
2. 
try1 - 5^20000 pruning? no dfs
try2 - dp?

a -> e
e -> a, i
i -> a, e, o, u
o -> i, u
u -> a
"""