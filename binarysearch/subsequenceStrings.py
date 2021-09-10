class Solution:
    def solve(self, s1, s2):

        if not s1:
            return True
        elif not s2:
            return False

        sameChars = []
        j = 0

        for i in range(len(s2)):
            if s2[i] == s1[j]:
                sameChars.append(s2[i])
                j += 1
                if len(sameChars) == len(s1):
                    break

        return s1 in ''.join(sameChars)
        