class Solution:
    def solve(self, words):

        if len(words) == 0:
            return 0
        elif len(words) == 1:
            return 1

        alliterationCount = 1
        currentCount = 1
        letter = words[0][0]

        for i in range(1, len(words)):

            if words[i][0] == letter:

                currentCount += 1
                
            else:

                if currentCount > alliterationCount:
                    alliterationCount = currentCount

                letter = words[i][0]
                currentCount = 1

        return alliterationCount if alliterationCount > currentCount else currentCount 
