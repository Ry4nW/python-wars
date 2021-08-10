class Solution:
    def solve(self, matrix):

        retMatrix = []
        length = len(matrix)

        for i in range(length):
            retMatrix.append([])

        for i in range(len(matrix[0])):

            column = []

            for j in range(length):
                column.append(matrix[j][i])

            column.sort()

            for j in range(length):
                retMatrix[j].append(column[j])
        
        return retMatrix
            