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

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(bTRoot.value)

for i in range(1, 6):
    print(eval(f'{alphabet[i]}Node.value'))



