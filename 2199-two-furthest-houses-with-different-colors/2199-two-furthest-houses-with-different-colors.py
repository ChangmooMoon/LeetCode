class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)

        ans = 0
        for i in range(N):
            l_dist = i if colors[i] != colors[0] else 0
            r_dist = N-1-i if colors[i] != colors[N-1] else 0
            ans = max(ans, l_dist, r_dist)

        return ans
        