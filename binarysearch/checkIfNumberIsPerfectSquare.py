class Solution:
    def solve(self, n):

        if n == 0:
            return True

        left = 1
        right = n

        while left <= right:
            mid = (left + right) >> 1

            if ((mid * mid) == n):
                return True
            
            if (mid * mid < n):
                left = mid + 1
            else:
                right = mid - 1
        
        return False