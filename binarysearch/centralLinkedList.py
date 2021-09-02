# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        head = node
        length = 0 

        while node:
            node = node.next
            length += 1
        
        count = 0

        while count != length // 2:
            head = head.next
            count += 1
        
        return head.val
        