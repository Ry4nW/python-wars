class Solution:
    def solve(self, prices, k):

        prices.sort()
        i = 0

        while i != len(prices) and k - prices[i] >= 0:
            k -= prices[i]
            i += 1
            print(i)

        return i 

    # Solution by jlin45655, uses enumerate()
    def solve(self, prices, k):
        prices.sort()
        total = 0
        for i, price in enumerate(prices):
            total += price
            if total > k:
                return i
        return len(prices)
        