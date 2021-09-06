# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        if not node:
            return True

        end, half = node, node
        head = node
        count = 0
        half1 = []
        half2 = []

        while end.next:
            if end.next.next != None:
                end = end.next.next
            else:
                end = end.next

            half = half.next
            count += 1

        while half.next:
            half1.append(str(half.val))
            half = half.next

        if count != 0:
            half1.append(str(half.val))
        
        if len(half1) > count:
            half1.pop(0)
        
        prev = None

        while count > 0:
            half2.append(str(head.val))
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            count -= 1

        return ''.join(half1) == ''.join(reversed(half2))
