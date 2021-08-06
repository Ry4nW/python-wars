class Solution:
    def solve(self, s):

        def isMatch(b1, b2):

            if b1 == '(' and b2 == ')':
                return True
            else:
                return False

        stack = []
        isBalanced = True
        index = 0

        while index < len(s) and isBalanced:

            paren = s[index]
            if paren == '(':
                stack.append(paren)
            else:
                if len(stack) == 0:
                    isBalanced = False
                    break
                else:
                    topBracket = stack.pop()

                    if not isMatch(topBracket, paren):
                        isBalanced = False
                        break
            
            index += 1
        
        if len(stack) == 0 and isBalanced:
            return True
        
        return False
        