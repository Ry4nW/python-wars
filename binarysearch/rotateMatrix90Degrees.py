class Solution:
    def solve(self, matrix):

        rotatedMatrix = []

        for i in reversed(range(len(matrix))):

            newRow = []

            for j in range(len(matrix)):
                newRow.append(matrix[j][i])
            
            rotatedMatrix.append(newRow)

        return rotatedMatrix
        