class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(op, cl, res):
            if(op > n or op < cl):
                return
            if(op == n and cl == n):
                ans.append(res)
                return
            
            dfs(op + 1, cl, res + '(')
            dfs(op, cl + 1, res + ')')
        
        dfs(1, 0, "(")
        return ans
        