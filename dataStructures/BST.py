class BTNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, root:BTNode = None) -> None:
        self.root = root
    
    def insert_node(self, val) -> BTNode:
        newNode = BTNode(val)
        def traverse(newNode, root) -> None:
            if root is not None:
                if root.val > newNode.val:
                    traverse(newNode, root.left)
                else:
                    traverse(newNode, root.right)
            if root.val > newNode.val:
                root.left = newNode
            else:
                root.right = newNode
        traverse(newNode, self.root)
        return newNode
        