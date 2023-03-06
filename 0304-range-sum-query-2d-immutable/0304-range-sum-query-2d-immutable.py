class NumMatrix:

    def __init__(self, matrix: List[List[int]]): # 숫자 매트릭스 init
        N, M = len(matrix), len(matrix[0])
        d = [[0] * (M + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                d[i][j] = matrix[i - 1][j - 1]
                d[i][j] += d[i][j - 1]
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                d[i][j] += d[i - 1][j]
        
        self.d = d
        print(d)
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: # 사각형 합 O(1)
        d = self.d
        return d[row2 + 1][col2 + 1] - d[row1][col2 + 1] - d[row2 + 1][col1] + d[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)