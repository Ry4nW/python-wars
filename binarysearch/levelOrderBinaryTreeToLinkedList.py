from collections import deque

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        if not root:
            return None
        
        queue = deque([])
        queue.append(root)
        levelOrder = []

        while len(queue) > 0:
            root = queue.popleft()
            levelOrder.append(root.val)

            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        
        head = LLNode(levelOrder[0])
        prev = head

        for i in range(1, len(levelOrder)):
            newNode = LLNode(levelOrder[i])
            prev.next = newNode
            prev = newNode
        
        return head
