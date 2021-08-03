class Solution:
    def solve(self, lists):

        largeSortedList = []

        for i in range(len(lists)):

            if lists[i] != []:

                for num in lists[i]:
                    largeSortedList.append(num)

        return sorted(largeSortedList)
        