class Queue:
	def __init__(self, array):
		self.elements = array

	# Adds a new element to the queue.
	def enq(self, element):
		self.elements.append(element)

	# Removes and returns the first (front) element from the queue.
	def deq(self):
		if not self.empty():
			return self.elements.pop(0)

	# Returns the first element in the queue.
	def peek(self):
		if not self.empty():
			return self.elements[0]

	# Checks if the queue is empty.
	def empty(self):
		return self.size() == 0

	# Finds the number of elements in the queue.
	def size(self):
		return len(self.elements)
