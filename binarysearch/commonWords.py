class Solution:
    def solve(self, s0, s1):

        list0 = set(s0.lower().split(' '))
        list1 = set(s1.lower().split(' '))
        
        if len(list0) > len(list1):
            minList = list0
            maxList = list1
        else:
            minList = list1
            maxList = list0

        uniqueWords = 0
        
        for word in minList:
            if word and word in maxList:
                uniqueWords += 1
            
        return uniqueWords
