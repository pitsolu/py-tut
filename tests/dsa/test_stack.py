from src.dsa.stack import Stack

shoppingList = Stack(["Bread", "Butter", "Milk"])

class TestStack:
	def test_push(self):
		assert shoppingList.peek() != "Eggs"
		shoppingList.push("Eggs")
		assert shoppingList.peek() == "Eggs"