from collections import deque

class Stack():
    def __init__(self, items: 'list[any]', maxsize) -> None:
        self.items: list[deque] = deque(items)
        self.maxsize: int = maxsize
        self.top: int = self.get_top()
    
    def get_stack(self) -> deque:
        return self.items

    def push(self, item) -> None or str:
        if len(self.items) < self.maxsize:
            self.items.append(item)	
            self.top = item			
        else:
            return 'Max capacity reached.'

    def pop(self) -> any:
        if self.items: 
            popped = self.items.pop()
            self.top = self.get_top()
            return popped
        return 'Stack is empty.'
    
    def is_empty(self) -> bool:
        return True if not self.items else False
    
    def get_top(self) -> any:
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is empty.'

stack = Stack([1, 2, 3, 4, 5], 6)
print(stack.top)
print(stack.push(6))
print(stack.top)
print(stack.pop())
print(stack.top)
