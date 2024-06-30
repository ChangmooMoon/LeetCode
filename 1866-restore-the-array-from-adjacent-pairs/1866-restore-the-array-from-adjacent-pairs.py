class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        a = defaultdict(list)
        ind = defaultdict(int)
        ans = []

        def dfs(prev, curr, ans):
            ans.append(curr)
            for nxt in a[curr]:
                if nxt != prev:
                    dfs(curr, nxt, ans)

        for u, v in adjacentPairs:
            a[u].append(v)
            a[v].append(u)
            ind[u] += 1
            ind[v] += 1

        for i, v in ind.items():
            if v == 1:
                dfs(None, i, ans)
                break
        
        return ans