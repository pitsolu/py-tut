import unittest

from src.dsa.stack import Stack

class StackTest(unittest.TestCase):
	def setUp(self):
		self.shoppingList = Stack(["Bread", "Butter", "Milk"])

	def test_push(self):
		self.shoppingList.push("Eggs")
		self.assertEqual(self.shoppingList.peek(), "Eggs")

if __name__ == '__main__':
    unittest.main()

