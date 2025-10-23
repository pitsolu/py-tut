class Stack:
	def __init__(self, array):
		self.elements = array;

	# Adds a new element on the stack.
	def push(self, item):
		self.elements.append(item)

	# Removes and returns the top element from the stack.
	def pop(self):
		if not self.empty():
			return self.elements.pop()

	#  Returns the top (last) element on the stack.
	def peek(self):
		if not self.empty():
			return self.elements[-1]

	# Checks if the stack is empty.
	def empty(self):
		return self.size() == 0

	# Finds the number of elements in the stack.
	def size(self):
		return len(self.elements)