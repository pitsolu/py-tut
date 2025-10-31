DSA - Data Structures & Algorithims
===

- Data types
- Basic Bitwise Operations
- String Operations
- Arrays
- [Linked Lists](#linked-list)
  - [Singly Linked](#singly)
  - [Doubly Linked](#doubly)
  - [Circular Linked](#circular)
- [Queues](#queue)
- [Stacks](#stack)
- Heaps
- Trees
  - Binary Trees
  - [Binary Search Trees](#binary-search-tree)
  - Tries
  - Self Balancing Trees
- Traversing Trees
  - Breadth First Search - BFS
  - Depth First Search - DFS
  - Preorder, Inorder, Postorder
- Graphs
  - Dijkstra's Algorithm / A\* Search
- Hash Maps
  - Handling Collisions
- Sorting algorithms
  - Insertion
  - Selection
  - Merge
  - Quick
- Time Complexities

### Stack

A stack is a data structure that can hold many elements, and the last element added is the 
first one to be removed (LIFO). 

There are 2 main operations in this data structure mainly `pop` and `push`

Run the code below in your `python` shell from the `root` directory (base directory)

```python
from src.dsa.stack import Stack

s = Stack(["a","b","c"])
s.push("d")
s.peek() # d
s.size() # 4
s.empty() # False
s.pop() # d
s.pop() # c
```

### Queue

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
There are 2 main operations in this data structure mainly `enqueue` and `dequeue`

```python
from src.dsa.queue import Queue
q = Queue(["a","b","c"])
q.enq("d")
q.peek() # a
q.size() # 4
q.empty() # False
q.deq() # a
q.deq() # b
q.deq() # c 
q.peek() # d
```

## Linked List

### Singly

A singly linked list is the simplest kind of linked lists. It takes up less space in memory because each node has only one address to the next node.

This data structure contains 5 operations `add` `delete` `put` and `lowest`

```python
from src.dsa.singly import Node, Singly

slist = Singly()

head = Node(7)
head.next = Node(13)
head.next.next = Node(5)
head.next.next.next = Node(17)
head.next.next.next.next = Node(9)

# Add operation
slist.add(head)
slist.show() # "7>>13>>5>>17>>9>>Null"

# Lowest operation
slist.lowest() # 5

# Delete operation
node = head.next.next # node 5
slist.delete(node)
slist.show() # "7>>13>>17>>9>>Null"

# Add operation
slist.add(Node(21))
slist.show() # "7>>13>>17>>9>>21>>Null"

# Insert operation
slist.put(Node(51), 2)
slist.show() # "7>>51>>13>>17>>9>>21>>Null"
```

### Doubly

A doubly linked list has nodes with addresses to both the previous and the next node, like in the image below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

### Circular

A circular linked list is like a singly or doubly linked list with the first node, the `head`, and the last node, the `tail`, connected.

## Trees

### Binary Search Tree

```python
from src.dsa.bst import *

root = insert(Node("b"), "c")
insert(root, "a")
show(root, 0) # show tree from level 0
#    -> c
# -> b
#    -> a
```