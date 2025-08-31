class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        a = [['.'] * n for _ in range(n)]
        l_check, r_check, col_check = set(), set(), set()
        ans = []

        def bt(r): # loop row
            if r == n:
                res = ["".join(row) for row in a]
                ans.append(res)
                return
            
            for c in range(n):
                if c in col_check or r+c in l_check or r-c in r_check:
                    continue

                col_check.add(c)
                l_check.add(r+c)
                r_check.add(r-c)
                a[r][c] = 'Q'
                bt(r+1)
                col_check.remove(c)
                l_check.remove(r+c)
                r_check.remove(r-c)
                a[r][c] = '.'
        
        bt(0)
        return ans
