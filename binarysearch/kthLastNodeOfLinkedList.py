# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):

        length = 0
        head = node

        while node.next:
            node = node.next
            length += 1
        
        while length > k:
            head = head.next
            length -= 1
        
        return head.val
        