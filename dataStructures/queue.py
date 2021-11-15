from linkedList import Node

class Queue:

    def __init__(self) -> None:
        self.front = None
        self.back = None
        
    def enqueue(self, item) -> bool:
        newNode = Node(item)

        if not self.is_empty(): self.front = newNode
        else: self.back.next = self.back.next = newNode

        self.back = newNode
    
    def dequeue(self) -> int or str:
        if self.front == None:
            return 'Failed operation -> Queue.dequeue()\nReason -> Queue is empty.'
        
        dequeuedVal = self.front.val
        self.front = self.front.next
        return dequeuedVal

    def peek(self) -> int or str:
        if self.is_empty(): 
            return 'Failed operation -> Queue.peek()\nReason -> Queue is empty.'
        return self.front.val
    
    def is_empty(self) -> int or str:
        return self.front == None
