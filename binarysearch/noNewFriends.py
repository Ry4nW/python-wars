class Solution:
    def solve(self, n, friends):

        for friend in range(n):

            hasFriend = False

            for pair in friends:

                if friend in pair:
                    hasFriend = True
                    break
            
            if not hasFriend:
                return False

        return True
