# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        count = 0
        currentNode = node

        while currentNode:
            count += 1
            currentNode = currentNode.next
        
        return count
        