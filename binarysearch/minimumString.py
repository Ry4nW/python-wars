from collections import Counter

class Solution:
    def solve(self, s, t):
        hashTable = Counter(s)
        changeCount = 0

        for i in t:
            try:
                if hashTable[i] > 0:
                    hashTable[i] -= 1
                    continue
                changeCount += 1
            except:
                changeCount += 1
        
        return changeCount
