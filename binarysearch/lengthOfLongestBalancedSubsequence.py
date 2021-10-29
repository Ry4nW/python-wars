from collections import deque

class Solution:
    def solve(self, s):
        count = 0
        stack = deque([])

        for i in s:
            if i == '(':
                stack.append(i)
            elif stack:
                stack.pop()
                count += 2

        return count
        