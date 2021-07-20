def linkedListToInteger():

    binary = ''

    while node:
        binary += str(node.val)
        node = node.next

    return int(binary, 2)
