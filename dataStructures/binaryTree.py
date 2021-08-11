class BinaryTree():

    def __init__(self, value):

        self.value = value
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, value):

        if self.leftChild == None:
            self.leftChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode
        
    def insertRight(self, value):

        if self.rightChild == None:
            self.rightChild = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

    def preOrderPrint(self, start, traversal):

        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preOrderPrint(start.leftChild, traversal)
            traversal = self.preOrderPrint(start.rightChild, traversal)
        
        return traversal

bTRoot = BinaryTree('a')
bTRoot.insertLeft('b')
bTRoot.insertRight('c')

bNode = bTRoot.leftChild
cNode = bTRoot.rightChild

bNode.insertRight('d')
cNode.insertLeft('e')
cNode.insertRight('f')

dNode = bNode.rightChild
eNode = cNode.leftChild
fNode = cNode.rightChild

print(bTRoot.preOrderPrint(bTRoot, ''))
