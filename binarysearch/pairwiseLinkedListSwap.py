# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        def LLSwap(head):
            if head != None and head.next != None:
                curVal = head.val
                head.val = head.next.val
                head.next.val = curVal
                LLSwap(head.next.next)
        
        LLSwap(node)
        return node
