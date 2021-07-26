class Solution:
    def solve(self, moves, x, y):

        xCoordinate = 0
        yCoordinate = 0

        for i in moves:

            if i == 'NORTH':
                yCoordinate += 1
            elif i == 'EAST':
                xCoordinate += 1
            elif i == 'SOUTH':
                yCoordinate += -1
            else:
                xCoordinate += -1
        
        return xCoordinate == x and yCoordinate == y

        