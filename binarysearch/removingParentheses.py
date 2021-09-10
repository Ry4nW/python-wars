class Solution:
    def solve(self, s):

        stack = []
        remove = 0

        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    remove += 1
                    continue
                elif stack.pop() == ')':
                    remove += 1
        
        return remove
               