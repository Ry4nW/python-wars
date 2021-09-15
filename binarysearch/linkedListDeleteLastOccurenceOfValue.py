# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):

        head = node
        lastOccurence = None
        lastOccurencePrev = None
        prev = None

        while node:
            if node.val == target:
                lastOccurence = node
                lastOccurencePrev = prev

            prev = node
            node = node.next

        if lastOccurencePrev:
            if lastOccurence.next:
                lastOccurencePrev.next =  lastOccurence.next
            else:
                lastOccurencePrev.next = None
        elif lastOccurence == head:

            head = head.next
            
        lastOccurence = None
         
        return head
        