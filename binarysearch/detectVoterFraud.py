class Solution:
    def solve(self, votes):

        voterIds = {}

        for vote in votes:

            try:
                if voterIds[vote[1]] == 1:
                    return True
            except:
                    voterIds[vote[1]] = 1

        return False 
            