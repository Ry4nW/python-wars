class Solution:
    def solve(self, arr):

        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2 + 1
            if arr[left] < arr[mid]:
                left = mid
            elif arr[left] > arr[mid]:
                right = mid - 1
            else:
                left += 1
                
        return arr[left]
