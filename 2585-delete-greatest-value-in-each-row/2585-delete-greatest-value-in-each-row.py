class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        ans = 0
        for i in range(len(grid[0])):
            hi = 0
            for row in grid:
                hi = max(hi, row[i])
            ans += hi
        
        return ans