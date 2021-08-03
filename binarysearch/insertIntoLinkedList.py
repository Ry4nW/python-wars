# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):

        count = 1
        newNode = LLNode(val)
        currentNode = head
        
        while count != pos:
            
            count += 1

            try:
                currentNode = currentNode.next
            except:
                newNode.next = head
                return newNode
        
        newNode.next = currentNode.next
        currentNode.next = newNode

        return head
        