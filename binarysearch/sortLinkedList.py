# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        if not node:
            return None

        nodes = []

        while node:
            nodes.append(node.val)
            node = node.next
        
        nodes.sort()
        head = LLNode(nodes[0])
        prev = head

        for i in range(1, len(nodes)):
            newNode = LLNode(nodes[i])
            prev.next = newNode
            prev = newNode
        
        return head
        