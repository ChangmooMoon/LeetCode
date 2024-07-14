class Solution:
    class UF:
        def __init__(self, n):
            self.n = n
            self.p = [_ for _ in range(n + 1)]
            self.rank = [1] * (n + 1)
        
        def find(self, x):
            while x != self.p[x]:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x
        
        def union(self, x, y):
            x, y = self.find(x), self.find(y)
            if x == y:
                return False
            if self.rank[x] > self.rank[y]:
                self.rank[x] += self.rank[y]
                self.p[y] = x
            else:
                self.rank[y] += self.rank[x]
                self.p[x] = y
            self.n -= 1
            return True
        
        def isConnected(self):
            return self.n <= 1


    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a, b = self.UF(n), self.UF(n)
        edge_num = 0

        for t, u, v in edges:
            if t == 3:
                edge_num += (a.union(u, v) | b.union(u, v))
            
        for t, u, v in edges:
            if t == 1:
                edge_num += a.union(u, v)
            elif t == 2:
                edge_num += b.union(u, v)
        
        return len(edges) - edge_num if a.isConnected() and b.isConnected() else -1
        