class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def tree_to_tuple(node):
    if node is None:
        return None
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)

def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)

def traverse_post_order(node):
    if node is None:
        return []
    return traverse_pre_order(node.left) + traverse_pre_order(node.right) + [node.key]

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

tree1 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

print(traverse_in_order(tree1))
print(traverse_pre_order(tree1))
print(traverse_post_order(tree1))

