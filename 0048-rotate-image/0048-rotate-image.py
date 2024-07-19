class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        
        # 1. transposed 2. reflect
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            for j in range(N//2):
                matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]