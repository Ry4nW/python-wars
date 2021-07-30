"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return True if not self.items else False
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is empty.'
        
    def get_stack(self):
        return self.items
