class Solution:
    def solve(self, matrix):

        transpose = []

        try:
            rowLength = len(matrix[0])
            
            for i in range(len(matrix)):

                newRow = []

                for j in range(0, rowLength):
                    newRow.append(matrix[j][i])
            
                transpose.append(newRow)
        
            return transpose
        
        except:
            return matrix


