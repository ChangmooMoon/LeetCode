class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        g = [[] for _ in range(n)] # 1000 * 1000
        for u, v in edges:
            g[u].append(v)

        def dfs(u, prev, visited):
            visited.add(u)
            for next in g[u]:
                if next not in visited:
                    ans[next].append(prev)
                    dfs(next, prev, visited)
        
        for i in range(n):
            dfs(i, i, set())
        
        return ans
