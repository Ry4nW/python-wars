class LLNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:

    def solve(self, head):

        prev = head.val - 1
        nextNode = head

        while nextNode:

            if nextNode.val <= prev:
                return False
            else:
                prev = nextNode.val
                nextNode = nextNode.next
        
        return True