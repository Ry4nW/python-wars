class Solution:
    def solve(self, string):

        encodedStr = ""

        data = string[0]
        count = 0

        for i in range(len(string)):

            if string[i] == data:
                count += 1

            else:

                data = string[i]
                encodedStr += "{count}".format(count=count) + string[i - 1]
                count = 1

            if i == len(string) - 1:
                c = str(count)
                encodedStr += c + data

        return "{count}".format(count=count) + data if len(encodedStr) == 0 else encodedStr