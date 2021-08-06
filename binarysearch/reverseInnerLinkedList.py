# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node, i, j):

        count = i
        cur = node
        firstNodePrev = None
        lastNode = None

        for _ in range(i):
            firstNodePrev = cur
            cur = cur.next

        lastNode = cur

        for _ in range(i, j + 1):
            lastNode = lastNode.next

        prev = lastNode

        while count != j + 1:

            count += 1
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        try:
            firstNodePrev.next = prev
        except:
            return prev

        return node
        