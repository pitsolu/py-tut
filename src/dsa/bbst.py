# Balance a Binary Search Tree
# ===
# Given a BST (Binary Search Tree) that may be unbalanced, the task is to 
# convert it into a balanced BST that has the minimum possible height.

# Python program to convert a left unbalanced BST to
# a balanced BST

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Inorder traversal to store elements of the
# tree in sorted order
def storeInorder(root, nodes):
    if root is None:
        return

    # Traverse the left subtree
    storeInorder(root.left, nodes)

    # Store the node data
    nodes.append(root.data)

    # Traverse the right subtree
    storeInorder(root.right, nodes)

# Function to build a balanced BST from a sorted array
def buildBalancedTree(nodes, start, end):
    # Base case
    if start > end:
        return None

    # Get the middle element and make it the root
    mid = (start + end) // 2
    root = Node(nodes[mid])

    # Recursively build the left and right subtrees
    root.left = buildBalancedTree(nodes, start, mid - 1)
    root.right = buildBalancedTree(nodes, mid + 1, end)

    return root

# Function to balance a BST
def balanceBST(root):
    nodes = []

    # Store the nodes in sorted order
    storeInorder(root, nodes)

    # Build the balanced tree from the sorted nodes
    return buildBalancedTree(nodes, 0, len(nodes) - 1)

# Print tree as level order
# from collections import deque

# def printLevelOrder(root):
#     if root is None:
#         print("N", end=" ")
#         return

#     queue = deque([root])
#     nonNull = 1

#     while queue and nonNull > 0:
#         curr = queue.popleft()

#         if curr is None:
#             print("N", end=" ")
#             continue
#         nonNull -= 1

#         print(curr.data, end=" ")
#         queue.append(curr.left)
#         queue.append(curr.right)
#         if curr.left:
#             nonNull += 1
#         if curr.right:
#             nonNull += 1

# Print Recursively
def showAt(node:Node, level:int=0):
    if node is None:
        return

    showAt(node.right, level + 1) # right subtree first
    print("    " * level + "-> " + str(node.data)) # current node
    showAt(node.left, level + 1) # left subtree

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    balancedRoot = balanceBST(root)
    # printLevelOrder(balancedRoot)
    showAt(balancedRoot, 0)
