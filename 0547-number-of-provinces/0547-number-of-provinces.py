class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        
        cnt = 0
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                self.dfs(N, isConnected, visited, i)
                cnt += 1
        
        return cnt
    
    def dfs(self, N, isConnected, visited, r):
        for c in range(N):
            if not visited[c] and isConnected[r][c]:
                visited[c] = True
                self.dfs(N, isConnected, visited, c)