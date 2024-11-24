class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        N = len(s)

        lookup = {}
        for i in range(N):
            x = 0
            for j in range(32):
                if i + j >= N:
                    break
                x = x << 1 | int(s[i + j])
                if x not in lookup:
                    lookup[x] = [i, i + j]
                if x == 0:
                    break

        ans = []
        for fi, se in queries:
            ans.append(lookup.get(fi^se, [-1, -1]))
        return ans