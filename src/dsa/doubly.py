class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def put(self, new_data, pos):
        new_node = Node(new_data)
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return self.head

        curr = self.head
        
        for _ in range(1, pos - 1):
            if curr is None:
                print("Position is out of bounds.")
                return self.head
            curr = curr.next

        if curr is None:
            print("Position is out of bounds.")
            return self.head

        new_node.prev = curr
        new_node.next = curr.next

        curr.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

        return self.head

    def backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.prev
        return " <- ".join(elements)

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <-> ".join(elements)
