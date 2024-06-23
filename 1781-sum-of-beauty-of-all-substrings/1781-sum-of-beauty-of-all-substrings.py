class Solution:
    def beautySum(self, s: str) -> int:
        N = len(s)
        
        ans = 0
        for i in range(N):
            counter = Counter()
            for j in range(i, N):
                counter[s[j]] += 1
                ans += max(counter.values()) - min(counter.values())
        
        return ans