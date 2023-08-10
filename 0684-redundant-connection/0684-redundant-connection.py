class Solution(object):
    def findRedundantConnection(self, edges):
        p = [_ for _ in range(1001)]
        
        def Find(p, x):
            if p[x] != x:
                p[x] = Find(p, p[x])
            return p[x]
        
        def Union(p, a, b):
            a, b = Find(p, a), Find(p, b)
            if a < b:
                p[b] = a
            else:
                p[a] = b
        
        for u, v in edges:
            if Find(p, u) == Find(p, v):
                return [u, v]
            Union(p, u, v)
        
"""
:type edges: List[List[int]]
:rtype: List[int]
"""
'''
1. undirected graph, tree + 1 edge, n 1000
2. uf 사이클 체크 1000 * (1000 + 1000) = 200만
'''	