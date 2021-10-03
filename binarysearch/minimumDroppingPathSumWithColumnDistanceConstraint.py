class Solution:
    def solve(self, matrix):

        path = 0

        for i in range(len(matrix)):
            sortedRow = sorted(matrix[i])
            index = matrix[i].index(sortedRow[0])
            minPath = float('-inf')
            try:
                for j in range(sortedRow[i + 1][index - 1], sortedRow[i + 1][index], sortedRow[i + 1][index + 1]):
                    try:
                        minPath = min(minPath, j)
                    except:
                        continue
                
                path += minPath
            except:
                break
        
        return path
        