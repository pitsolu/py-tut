DSA - Data Structures & Algorithims
===

- Data types
- Basic Bitwise Operations
- String Operations
- Arrays
- Linked Lists
  - Singly Linked
  - Doubly Linked
  - Circular Linked
- [Queues](#queue)
- [Stacks](#stack)
- Heaps
- Trees
  - Binary Trees
  - Binary Search Trees
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