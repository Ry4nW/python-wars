def sum_two_lists(self, llist):
    firstNum = []
    secondNum = []

    cur = self.head

    while cur:
        firstNum.prepend(str(cur.val))
        cur = cur.next
    
    while llist:
        secondNum.prepend(str(llist.val))
        llist = llist.next
    
    return int(''.join(firstNum)) + int(''.join(secondNum))

