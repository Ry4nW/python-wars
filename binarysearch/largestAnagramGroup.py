class Solution:
    def solve(self, words):

        for i in range(len(words)):
            words[i] = ''.join(sorted(words[i]))
        
        longestAnagramCount = 0
        curCount = 1
        wordsSet = list(set(words))
        
        for word in wordsSet:

            longestAnagramCount = words.count(word) if words.count(word) > longestAnagramCount else longestAnagramCount
        
        return longestAnagramCount if longestAnagramCount > curCount else curCount
