class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        N = len(primes)
        ans = [1]
        cnt = [0] * N
        d = primes[:]
    
        for i in range(1, n):
            target = min(d)
            ans.append(target)
            
            for j in range(N):
                if d[j] == target:
                    cnt[j] += 1
                    d[j] = ans[cnt[j]] * primes[j]
        
        # print(ans)
        return ans[n - 1]
        
        
"""
1. n = 100000, len(primes) = 100
"""