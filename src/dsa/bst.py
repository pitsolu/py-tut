# A Binary Search Tree (BST) is a data structure where each node has at most two children, 
# and the value of each node is greater than all values in its left subtree and less than 
# all values in its right subtree. This ordering allows for efficient searching, insertion, 
# and deletion, with an average time complexity of O(log n).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root:Node, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# Print Tree
def show(head):
    showAt(head, 0)

# Print Recursively
def showAt(node:Node, level:int=0):
    if node is None:
        return

    showAt(node.right, level + 1) # right subtree first
    print("    " * level + "-> " + str(node.value)) # current node
    showAt(node.left, level + 1) # left subtree