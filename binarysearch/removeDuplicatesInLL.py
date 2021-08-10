# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Own solution w/ try-except block
    def solve(self, node):

        values = {}
        prev = None
        cur = node

        while cur:

            nxt = cur.next

            try:
                test = values[cur.val]

                # Test variable will pass if we have a duplicate. 
                cur = None

                if prev != None:
                    prev.next = nxt
            except:
                values[cur.val] = 0
                prev = cur
            
            cur = nxt
        
        return node
    
    # educative.io's solution with conditionals, faster than declaring {test}
    def solve2(self, node):

        cur = node
        prev = None
        dup_values = dict()

        while cur:
            if cur.val in dup_values:
            # Remove node:
                prev.next = cur.next
                cur = None
            else:
            # Have not encountered element before.
                dup_values[cur.val] = 1
                prev = cur
            
            cur = prev.next
        
        return node
