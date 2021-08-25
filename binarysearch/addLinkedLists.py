# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        
        num1 = ''
        num2 = ''

        while l0:
            num1 += str(l0.val)
            l0 = l0.next
        
        while l1:
            num2 += str(l1.val)
            l1 = l1.next
        
        LLSum = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = LLNode(int(LLSum[0]))
        prev = head

        for i in range(1, len(LLSum)):
            newNode = LLNode(int(LLSum[i]))
            prev.next = newNode
            prev = newNode
        
        return head
        