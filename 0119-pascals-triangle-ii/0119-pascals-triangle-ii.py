class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (1+rowIndex)
        
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                ans[i-j] += ans[i-1-j]
        
        return ans
