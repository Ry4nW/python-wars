class Solution:
    def solve(self, matrix):

        try:
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    if matrix[j][i] == 1:
                        return i
        except:
            pass

        return -1
        