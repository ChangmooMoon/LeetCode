class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def dfs(i, j):
            tmp = float('inf')
            for k in range(i+1, j):
                tmp = min(tmp, values[i] * values[k] * values[j] + dfs(i,k) + dfs(k,j))
            return tmp if tmp != float('inf') else 0

        return dfs(0, len(values)-1)