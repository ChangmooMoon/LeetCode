class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(picked, idx):
            if len(picked) == k:
                ans.append(picked.copy())
                return
            
            for i in range(idx, n + 1):
                picked.append(i)
                dfs(picked, i + 1)
                picked.pop()

        dfs([], 1)
        return ans
