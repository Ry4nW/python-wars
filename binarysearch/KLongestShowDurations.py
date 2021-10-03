class Solution:
    def solve(self, shows, durations, k):
        showsDict = { show:0 for show in shows }
        for i in range(len(shows)):
            showsDict[shows[i]] += durations[i]
        sortedShows = sorted(showsDict.values(), reverse=True)
        retSum = 0
        for i in range(k):
            retSum += sortedShows[i]
        return retSum
