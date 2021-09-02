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

    prev = None
    head = None

    def solve(self, root):

        def solve1(root):

            if root:
                solve1(root.left)

                cur = LLNode(root.val)
                if self.prev:
                    self.prev.next = cur
                
                if not self.head:
                    self.head = cur
                self.prev = cur

                solve1(root.right)
            
            return root
        
        solve1(root)
        return self.head
