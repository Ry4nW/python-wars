class Solution:
    def solve(self, matrix):

        for list in matrix:

            for i in range(len(list)):

                if list[i] == 0:
                    list[i] = 1
                else:
                    list[i] = 0
                    
            list = list.reverse()

        return matrix