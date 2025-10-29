from src.dsa.singly import Node, Singly

slist = Singly()

a = Node(7)
a.next = Node(13)
a.next.next = Node(5)
a.next.next.next = Node(17)
a.next.next.next.next = Node(9)

def test_show():
	slist.add(a)
	assert slist.show() == "7>>13>>5>>17>>9>>Null"

def test_lowest():
	assert slist.lowest() == 5

def test_remove():
	node = a.next.next # node 5
	slist.delete(node)
	assert slist.show() == "7>>13>>17>>9>>Null"

def test_add():
	slist.add(Node(21))
	assert slist.show() == "7>>13>>17>>9>>21>>Null"

def test_put():
	slist.put(Node(51), 2)
	assert slist.show() == "7>>51>>13>>17>>9>>21>>Null"