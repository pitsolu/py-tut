class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

# A doubly linked list has each node with data and two links to the next and previous nodes, 
# allowing traversal in both directions.

# DELETE the last node from the end of the doubly linked list
def pop(head:Node):
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next

    del_node = current.next
    current.next = None
    del del_node
    return head

# DELETE the first node from the beginning of the doubly linked list
def unshift(head:Node):
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    new_head = head.next
    new_head.prev = None
    del head
    return new_head

# DELETE the node at a given position from the doubly linked list
def rm(head:Node, position:int):
    if head is None:
        print("Doubly linked list is empty")
        return None

    if position < 0:
        print("Invalid position")
        return head

    if position == 0:
        if head.next:
            head.next.prev = None
        return head.next

    current = head
    # count = 0
    # while current and count < position:
    #     current = current.next
    #     count += 1

    for _ in range(position):
        current = current.next

    if current is None:
        print("Position out of range")
        return head

    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next

    del current
    return head

# INSERT a node before a given node in a doubly linked list
# def put(head:Node, node:Node, new_node:Node):
def put(node:Node, new_node:Node):
# def put(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    # current = head
    # while current:
    #     if current.data == node.data:
    #         break
    #     current = current.next

    # current.prev = new_node
    # current.next = node

    # return  head

    new_node.prev = node.prev
    new_node.next = node

    if node.prev:
        node.prev.next = new_node

    node.prev = new_node
    return node

# INSERT a new node at the end of the doubly linked list
def append(head:Node, new_node:Node):
# def append(head, data):
#     new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head

# INSERT a new node at the beginning of the doubly linked list
def shift(head:Node, new_node:Node):
# def shift(head, data):
    # new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# TRAVERSE the doubly linked list and print its elements
def show(head:Node):
    current = head
    ls = []
    while current:
      # Print current node's data
        ls.append(current.data)
        ls.append(" <-> ")  
        # Move to the next node
        current = current.next  
    ls.append("None")
    return "".join(ls)

def makeLs(ls:list):
    nodes = {}
    head = None
    for item in ls:
        head = append(head, Node(item))
    return head

def nodeLs(head:Node):
    nodes = {}
    current = head
    while current:
        nodes[current.data] = current
        current = current.next
    return nodes

# class Doubly:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#         new_node.prev = last

#     def prepend(self, data):
#         new_node = Node(data)
#         if self.head:
#             self.head.prev = new_node
#         new_node.next = self.head
#         self.head = new_node

#     def forward(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.next
#         print("None")

#     def backward(self):
#         current = self.head
#         if not current:
#             print("None")
#             return
#         while current.next:
#             current = current.next
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.prev
#         print("None")