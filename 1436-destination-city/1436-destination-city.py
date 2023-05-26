class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        g = {}
        for p in paths:
            g[p[0]] = p[1]
        
        st = paths[0][0]
        while True:
            if g.get(st) is None:
                break
            st = g[st]
        
        return st