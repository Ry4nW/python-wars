class Solution:
    def solve(self, s):

        def bracketMatch(brckt, popped):
            if (brckt == ']' and popped == '[') or (brckt == ')' and popped == '(') or (brckt == '}' and popped == '{'):
                return True
            
            return False

        stack = []
        openBrackets = ('[', '(', '{')
        isBalanced = True

        for i in s:
            
            if i in openBrackets:
                stack.append(i)
            else:

                if len(stack) == 0:
                    isBalanced = False
                    break
                else:
                    popped = stack.pop()

                    if not bracketMatch(i, popped):
                        isBalanced = False
                        break
        
        if isBalanced and len(stack) == 0:
            return True

        return False
