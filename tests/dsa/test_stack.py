from src.dsa.stack import Stack

shoppingList = Stack(["Bread", "Butter", "Milk"])

class TestStack:
	def test_push(self):
		assert shoppingList.peek() != "Eggs"
		shoppingList.push("Eggs")
		assert shoppingList.size() == 4
		assert shoppingList.peek() == "Eggs"

	def test_pop(self):
		assert shoppingList.pop() == "Eggs"
		assert shoppingList.peek() == "Milk"
		shoppingList.pop() # Milk
		shoppingList.pop() # Butter
		shoppingList.pop() # Bread
		assert shoppingList.empty() == True