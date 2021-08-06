class LLNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:

    def solveIteratively(self, node):

        prev = None
        cur = node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
    
    def solveRecursively(self, node):

        def reverseRecursively(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return reverseRecursively(cur, prev)

        return reverseRecursively(cur = node, prev = None)
        