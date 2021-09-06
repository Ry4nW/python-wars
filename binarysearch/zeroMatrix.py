class Solution:
    def solve(self, matrix):

        row = {}
        col = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cur = matrix[i][j]
                if cur == 0:
                    if i not in row:
                        row[i] = 1

                    if j not in col:
                        col[j] = 1

        zeroRow = [0 for _ in matrix[0]]

        for row in row:
            matrix[row] = zeroRow.copy()
    
        for col in col:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        return matrix
