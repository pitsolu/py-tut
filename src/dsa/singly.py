class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# A singly linked list is the simplest kind of linked lists. 
# It takes up less space in memory because each node has only one address to the next node
class Singly:
  def __init__(self):
    self.head = None

  def show(self):
    currentNode = self.head
    ll = []
    while currentNode:
      ll.append(str(currentNode.data) + ">>")
      currentNode = currentNode.next
    ll.append("Null")
    return "".join(ll)

  def lowest(self):
    minValue = self.head.data
    currentNode = self.head.next
    while currentNode:
      if currentNode.data < minValue:
        minValue = currentNode.data
      currentNode = currentNode.next
    return minValue

  def add(self, new_node:Node):
    # new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node

  def delete(self, node:Node):
    if self.head == node:
      return self.head.next

    curr_node = self.head
    while curr_node.next and curr_node.next != node:
      curr_node = curr_node.next

    if curr_node.next is None:
      return self.head

    curr_node.next = curr_node.next.next
    return self.head

  def put(self, new_node:Node, position):
    if position == 1:
      new_node.next = self.head
      return new_node

    curr_node = self.head
    for _ in range(position - 2):
      if curr_node is None:
        break
      curr_node = curr_node.next

    new_node.next = curr_node.next
    curr_node.next = new_node
    return self.head