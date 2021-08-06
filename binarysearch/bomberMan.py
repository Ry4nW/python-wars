class Solution:
    def solve(self, matri):

        matrix = []
        length = len(matri)
        damagedRow = []

        for i in range(len(matri)):

            matrix.append([])

            for j in range(len(matri[i])):
                matrix[i].append(matri[i][j])

        for i in range(len(matrix[0])):
            damagedRow.append(1)

        for i in range(length):

            for cell in range(len(matrix[i])):

                if matri[i][cell] == 1:

                    matrix[i] = damagedRow.copy()

                    for columnCell in range(len(matrix)):
                        matrix[columnCell][cell] = 1

        safeCells = 0 

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                if matrix[i][j] == 0:
                    safeCells += 1
        
        return safeCells
