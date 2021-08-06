# Attempt, TLEs on submission
class Solution:
    def solve(self, matrix):

        returnMatrix = []
        zeroRow = []

        for i in range(len(matrix)):
            returnMatrix.append([])

            for j in range(len(matrix[i])):
                returnMatrix[i].append(matrix[i][j])

        for _ in range(len(matrix[0])):
            zeroRow.append(0)

        for row in range(len(matrix)):

            for cell in range(len(matrix[row])):

                if matrix[row][cell] == 0:
                    returnMatrix[row] = zeroRow.copy()
                
                    for i in range(len(matrix)):
                        returnMatrix[i][cell] = 0
        
        return returnMatrix
